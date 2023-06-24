import React, { useState } from 'react';
import './StartPage.css';

const StartPage = () => {
  const [textInput, setTextInput] = useState('');
  const [selectedFile, setSelectedFile] = useState(null);

  const handleTextInputChange = (event) => {
    setTextInput(event.target.value);
  };

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // Process the text input and uploaded file as needed
    console.log('Text Input:', textInput);
    console.log('Selected File:', selectedFile);
    // Reset the form fields
    setTextInput('');
    setSelectedFile(null);
  };

  return (
    <div className='container-startpage'>
      <h1 className='startpage-title'>Copy - Paste your text or simply upload your document!</h1>
      <form className='startpage-form' onSubmit={handleSubmit}>
        <div>
          <label htmlFor="textInput" className='startpage-label'>Text Input:</label>
          <textarea
            className="startpage-textarea"
            value={textInput}
            onChange={handleTextInputChange}
            rows={10} // Adjust the number of rows as needed
            />
        </div>
        <div>
          <label htmlFor="fileUpload" className='startpage-label'>Upload File:</label>
          <input
            type="file"
            id="fileUpload"
            onChange={handleFileUpload}
            className='startpage-input'
          />
        </div>
        <button type="submit" className='startpage-button'>Submit</button>
      </form>
    </div>
  );
};

export default StartPage;
