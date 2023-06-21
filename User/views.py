from django.shortcuts import render
from .forms import InputForm
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import Docx2txtLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from random import shuffle
import openai
from langchain.text_splitter import CharacterTextSplitter
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os


openaikey = "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"
openai.api_key = openaikey
os.environ['OPENAI_API_KEY'] = openaikey
storagepath = './quizzx/storage/'

def home_view(request):
    form = InputForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            
            #get inputs from the form
            files = [request.FILES.get('file', None)]
            text = form.cleaned_data['text']
            topics = form.cleaned_data['topics']
            topics = [topic.strip() for topic in topics.split(',')]

            pages = []

            for file in files:
                # write files onto disk for further processing
                default_storage.save(storagepath + file.name, ContentFile(file.read()))

                # read the file into langchain dataloader
                if file.name.endswith('.pdf'):
                    loader = PyPDFLoader(storagepath + file.name)
                    pages.extend(loader.load_and_split())
                
                # delete the file from storage
                default_storage.delete(storagepath + file.name)
                
            #shuffle pages
            shuffle(pages)
            
            #generate faiss index
            faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings())

            mcqshtml = ''

            for topic in topics:
                temp = [item.page_content for item in faiss_index.similarity_search(topic)]
                docs = ''.join(temp)
                
                prompt = f"Using the documents below, generate 5 MCQs on the topic: {topic}. Output mcqs in HTML such that when passed onto a website can perfectly display HTML. Also in the end display the answer key as html\n\n{docs}"

                response = openai.Completion.create(
                    engine='text-davinci-003',
                    prompt=prompt,
                    max_tokens = 760,
                    temperature = 1.27,
                )

                mcqshtml += response['choices'][0]['text']

            return render(request, 'home.html', {'mcqshtml': mcqshtml, 'form': form})

    return render(request, 'home.html', context={'form': form})
