from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from random import shuffle, randint
import openai
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from django.core.files.storage import default_storage
from django.core.mail import send_mail
from django.core.files.base import ContentFile
from docx import Document
import time
import os
import fitz

openai.api_key = os.environ.get('OPENAI_API_KEY')
storagepath = './quizzx/storage/'
ALLOWED_EXTENSIONS = ['.pdf', '.doc', '.docx', '.txt']


# returns homepage
def home_view(request):
    return render(request, 'home.html')

# checks for valid file extensions
def valid_file_extension(filename):
    return any(filename.endswith(extension) for extension in ALLOWED_EXTENSIONS)

def image_or_text_pdf_classifier(pdf_file):
    with open(pdf_file,"rb") as f:
        pdf = fitz.open(f)
        res = 0
        for page in pdf:
            image_area = 0.0
            text_area = 0.0
            for b in page.get_text("blocks"):
                if '<image:' in b[4]:
                    r = fitz.Rect(b[:4])
                    image_area = image_area + abs(r)
                else:
                    r = fitz.Rect(b[:4])
                    text_area = text_area + abs(r)
                    
            if text_area == 0.0:  res = 1
        
        return res
        
        

def read_file(storagepath, filename):
    chunks = []
    
    # read the file into langchain dataloader
    if filename.endswith('.pdf'):
        # 0:    pdf is text-based, 1:   pdf is image-based,     2: pdf has both image and text
        pdf_class = image_or_text_pdf_classifier(storagepath+filename)
        
        # if pdf is imagebased, this will make an ocrversion of the pdf file
        if pdf_class==1:    return None
                
        documents = fitz.open(storagepath + filename)
        for doc in documents: chunks.append(doc.get_text()) 

    elif filename.endswith('.doc') or filename.endswith('.docx'):
        # read the doc or docx files
        doc = Document(storagepath + filename)
        for para in doc.paragraphs:
            chunks.append(para.text)
            
    elif filename.endswith('.txt'):
        # read the txt file
        with open(storagepath + filename, 'r') as f:
            chunks.append(f.read())
               
    return chunks


# code to generate mcqs without important topics
def make_mcqs_without_topics(chunks):
    mcqs = []
    
    # we join the chunks
    chunks = "".join(chunks)
    
    # generate random indexes
    indexes = [randint(0, len(chunks)) for _ in range(12)]
    
    prompt = f"""[START]\n{",".join([chunks[i:i+600] for i in indexes])}[END]
        
    Using the documents below, generate at least 10 multiple-choice questions using the snippets provided above. Do not use external knowledge and generate questions with medium difficulty.

    """ + """Each question should be separated by a comma and should be in a valid JSON that looks like this {"question": "..","options": ["..",".."],"answer": ".."}, {"question": "..","options": ["..",".."],"answer": ".."} 
                
    Do not output any other characters and do not deviate from the desired output.
                
    MCQS="""

    response = openai.Completion.create(
        engine='gpt-3.5-turbo-instruct',
        prompt=prompt,
        max_tokens = 1500,
        temperature = 0.8
    )
    
    response = response['choices'][0]['text']

    mcqs.extend(eval('['+response+']'))
    
    return mcqs

# code to generate mcqs with important topics
def make_mcqs_with_topics(chunks, topics):
    mcqs = []
    
    # generate faiss index
    faiss_index = FAISS.from_texts(chunks, OpenAIEmbeddings())

    for topic in topics:        
        relevant_chunks = [item for item in faiss_index.similarity_search(topic, k = 2)]
        relevant_chunks = [chunk.page_content for chunk in relevant_chunks]
        relevant_chunks = ''.join(relevant_chunks)

        prompt = f"""Using the documents below, generate as many as possible (max 10) MCQs on the topic: {topic}.""" + \
            """Each question should be separated by a comma and should be in a valid JSON that looks like this {"question": "..","options": ["..",".."],"answer": ".."}\nDo not output any other characters and output plain JSON.""" + \
            f"""\n[START]\n{relevant_chunks}[END] MCQS="""

        response = openai.Completion.create(
            engine='gpt-3.5-turbo-instruct',
            prompt=prompt,
            max_tokens=800,
            temperature=0.8
        )

        response = response['choices'][0]['text']
        response = response.replace('\n', '')
        response = response.replace("\'", "")

        mcqs.extend(eval('['+response+']'))
        
    return mcqs

# handles the post requests made by generator page
def gen_view(request):
    if request.method == 'POST':
        
        # if user is not authenticated, then only give the user 3 tries
        if not request.user.is_authenticated:
            usage_counter = request.session.get('usage_counter', 0)

            # Increment the usage counter
            if usage_counter < 3:   request.session['usage_counter'] = usage_counter + 1
            else:
                messages.error(request, 'Please log in to continue further.')
                return redirect('gen')
        
        # Track start time
        start_time = time.time()
        
        # get inputs from the form
        file = request.FILES.get('document', None)
        topics = request.POST.get('topics','')
        
        # if any file is not found or invalid file format then return an error
        if not file or not valid_file_extension(file.name):
            messages.error(request, 'Invalid file type. Please upload a .pdf, .doc, .docx, or .txt file.')
            return redirect('GET','gen')
        
        # write files onto disk for further processing
        default_storage.save(storagepath + file.name, ContentFile(file.read()))
        
        # shread the docuemnts into smaller chunks nad shuffle them
        chunks = read_file(storagepath, file.name)
        
        if not chunks:
            messages.error(request, 'This is a scanned PDF. Please upload a text-based PDF.')
            return redirect('gen')
        
        shuffle_in_chunks(chunks)

        # delete the file from storage
        default_storage.delete(storagepath + file.name)
        
        # if important topics are not specified
        if topics == '':  mcqs = make_mcqs_without_topics(chunks)
        # if important topics are specified
        else: 
            topics = topics.split()
            mcqs = make_mcqs_with_topics(chunks, topics)
        
        end_time = time.time()
        total_time = round(end_time-start_time, 2)

        return render(request, 'gen.html', {'mcqs': mcqs, 'time': total_time, 'filename': file.name})
    

    return render(request, 'gen.html')


# randomly shuffles the chunks
def shuffle_in_chunks(arr):
    chunk_size = max(len(arr) // 5,1)

    shuffled = []

    for i in range(0, len(arr), chunk_size):
        chunk = arr[i:i+chunk_size]
        shuffle(chunk)
        shuffled.extend(chunk)

    return shuffled


# code for contact me form
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        
        if form.is_valid():
            # Extract form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            subject = f"New message from {name}"
            message_body = f"From: {name} <{email}>\n\n{message}"

            send_mail(subject, message_body, 'quizzx.staff@gmail.com', ['namannir@buffalo.edu'])

            # Redirect to a success page or the same page with a success message.
            messages.error(request, 'We have received your message!')
            
            return redirect('contact-us')

    else:
        form = ContactForm()

    return render(request, 'contact-us.html', {'form': form})
    

# code for contact me form
def about_view(request):
    return render(request, 'about-us.html')
    
