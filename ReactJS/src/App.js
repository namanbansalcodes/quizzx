import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './HomePage/HomePage';
import LoginPage from './LoginPage/LoginPage';
import PricingPage from './PricingPage/PricingPage';
import NavBar from './NavBar';
import StartPage from './StartPage/StartPage';
import Footer from './Footer'
import ContactPage from './ContactPage/ContactPage';
import AboutPage from './AboutPage/AboutPage';

function App() {
  return (
    <Router>
    <NavBar />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/pricing" element={<PricingPage />} />
        <Route path="/start" element={<StartPage />} />
        <Route path="/contact" element={<ContactPage />} />
        <Route path="/about" element={<AboutPage />} />
      </Routes>
      <Footer />
      <div className='bottom'></div>
    </Router>
  );
}

export default App;
