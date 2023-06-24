import React, { useState } from 'react';
import './ContactPage.css'

const ContactPage = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission logic here
    // You can access the form values using the 'name', 'email', and 'description' state variables
    console.log('Form submitted:', { name, email, description });
    // Reset the form fields
    setName('');
    setEmail('');
    setDescription('');
  };

  return (
    <div className='containers'>
      <h1>Contact Us</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label className='label' htmlFor="name">Name:</label>
          <input className='input'
            type="text"
            id="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </div>
        <div>
          <label className='label' htmlFor="email">Email:</label>
          <input className='input'
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <div>
          <label className='label' htmlFor="description">Description:</label>
          <textarea className='textarea'
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          ></textarea>
        </div>
        <button className='button' type="submit">Submit</button>
      </form>
    </div>
  );
};

export default ContactPage;
