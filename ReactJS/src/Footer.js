import React from 'react';
import './Footer.css'
import { Link } from 'react-router-dom';

const Footer = () => {
  return (
    <footer className="footer">
    <div className="footer-logo">
    <div className="footer-logo-image"></div>
    </div>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/login">Login</Link>
          </li>
          <li>
            <Link to="/pricing">Pricing</Link>
          </li>
          <li>
            <Link to="/contact">Contact</Link>
          </li>
          <li>
            <Link to="/about">About</Link>
          </li>
          <li>
            <Link to="/start">Start for free!</Link>
          </li>
          <p>© 2023 Quizzx. All rights reserved.</p>
        </ul>
      </nav>
    </footer>
  );
};

export default Footer;
