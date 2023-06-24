import React from 'react';
import './HomePage.css';
import homeImage from '../Assets/home-image.png';
import { Link } from 'react-router-dom';
import studentImage from '../Assets/student.png';
import educatorImage from '../Assets/educator.png';
import creatorImage from '../Assets/creator.png'

const HomePage = () => {
  return (
    <div>
      <main>
        <h1>Welcome to Quizzx - The most powerful AI Quiz Generator Tool!</h1>
        <div className="how-it-works">
          <div className="description">
            <h2>How It Works</h2>
            <p className='how-it-works-description'>
              Quizzx uses Langchain and GPT to generate powerful AI quizzes. With the advanced capabilities of these technologies, Quizzx can create engaging and intelligent quizzes for various topics. Simply upload the PDF or text as a reference!
            </p>
            <Link to="/login" className="try-it-button">
              Try It Out !
            </Link>
          </div>
          <div className="homeImage">
            <img src={homeImage} alt="How It Works" />
          </div>
        </div>
        <div className="who-is-it-for">
          <h2>Who Is It For?</h2>
          <div className="use-case-container">
            <div className="use-case">
            <img src={studentImage} alt="Students" className="use-case-image-student" />
              <h3>Students</h3>
              <p>
                Quizzx provides students with an interactive and engaging way to test their knowledge, prepare for exams, and enhance their learning experience.
              </p>
            </div>
            <div className="use-case">
            <img src={educatorImage} alt="Educators" className="use-case-image-educator" />
              <h3>Educators</h3>
              <p>
                Quizzx assists educators in creating customized quizzes and assessments, saving time and effort while maintaining high-quality educational content.
              </p>
            </div>
            <div className="use-case">
            <img src={creatorImage} alt="Creators" className="use-case-image-creator" />
              <h3>Content Creators</h3>
              <p>
                Quizzx empowers content creators to generate dynamic quizzes that can be used in e-learning platforms, websites, and online courses to engage their audience.
              </p>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default HomePage;
