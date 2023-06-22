import React from 'react';
import { Link } from 'react-router-dom';
import './NavBar.css'
const Navbar = () => {
  return (
    <header>
      <div className="logo">
        <div className="logo-image"></div>
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
        </ul>
      </nav>
    </header>
  );
};

export default Navbar;
