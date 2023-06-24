import React from 'react';
import './AboutPage.css'

const AboutPage = () => {
  return (
    <div className="container1">
      <h1 className='h1'>About Us</h1>
      <div className="about-content">
        <div className="about-motivation">
          <h2 className='h2'>Motivation</h2>
          <p className='p'>
            Quizzx was created with the aim to provide a powerful AI Quiz Generator Tool that can assist users in generating quizzes quickly and efficiently. We understand the importance of quizzes in various domains, such as education, training, and assessments, and our tool is designed to simplify the process of quiz creation.
          </p>
          <p className='p'>
            Whether you are an educator, a content creator, or someone who needs to create quizzes regularly, Quizzx can save you valuable time and effort by leveraging the capabilities of artificial intelligence.
          </p>
        </div>
        <div className="about-technologies">
          <h2 className='h2'>Technologies Used</h2>
          <h3 className='h3'>GPT (Generative Pre-trained Transformer)</h3>
          <p className='p'> 
            GPT is a state-of-the-art language model that utilizes deep learning techniques to generate human-like text. It has been trained on a vast amount of text data, enabling it to understand and generate coherent and contextually relevant responses.
          </p>
          <h3 className='h3'>Langchain</h3>
          <p className='p'>
            Langchain is a cutting-edge technology that combines natural language processing (NLP) and blockchain. It provides secure and decentralized language-related services, ensuring data privacy, authenticity, and integrity in the context of language-based applications.
          </p>
        </div>
      </div>
    </div>
  );
};

export default AboutPage;
