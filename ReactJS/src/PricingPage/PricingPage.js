import React from 'react';
import { Link } from 'react-router-dom';
import './PricingPage.css';

const PricingPage = () => {
  return (
    <div className="container">
      <h1>Pricing</h1>
      <div className="pricing-cards">
        <div className="card">
          <h2>Quizzx Free</h2>
          <p>You get 10 free credits.</p>
          <div className="checklist">
            <h3>Features:</h3>
            <ul>
              <li>Basic functionality</li>
              <li>Limited access to premium features</li>
              <li>Community support</li>
            </ul>
          </div>
          <Link to="/login" className="btn-get-started">Get Started</Link>
        </div>
        <div className="card">
          <h2>Quizzx Pro</h2>
          <p>Subscription of $10/month.</p>
          <div className="checklist">
            <h3>Features:</h3>
            <ul>
              <li>Full access to premium features</li>
              <li>Priority support</li>
              <li>Advanced analytics</li>
            </ul>
          </div>
          <Link to="/login" className="btn-get-started">Get Started</Link>
        </div>
      </div>
    </div>
  );
};

export default PricingPage;
