import React, { useState } from 'react';
import Modal from 'react-modal';
import './PostSection.css';
// Import the CSS file

Modal.setAppElement('#root'); // Set the root element for accessibility

function PostSection() {
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [postContent, setPostContent] = useState('');
  const [mediaFile, setMediaFile] = useState(null);

  const openModal = () => {
    setModalIsOpen(true);
  };

  const closeModal = () => {
    setModalIsOpen(false);
    // Clear input fields when closing modal
    setPostContent('');
    setMediaFile(null);
  };

  const handleContentChange = (e) => {
    setPostContent(e.target.value);
  };

  const handleMediaChange = (e) => {
    setMediaFile(e.target.files[0]);
  };

  const handleSubmit = () => {
    // Perform actions like sending the post content and media file to a server
    console.log('Posting content:', postContent);
    if (mediaFile) {
      console.log('Uploaded media file:', mediaFile);
    }
    // Clear input fields after posting
    setPostContent('');
    setMediaFile(null);
    // Close modal after posting
    closeModal();
  };

  return (
    <div>
      <button onClick={openModal} className='train'>Create Post</button>
      <Modal
        isOpen={modalIsOpen}
        onRequestClose={closeModal}
        contentLabel="Create Post Modal"
      >  
        <h2 className='puma'>Create Post</h2>
         <br /><br /> 
        
        < div className="search-bar-container">
        
       
        <textarea
          placeholder="What's on your mind?"
          value={postContent}
          onChange={handleContentChange}
          rows={30}
          cols={100}
        />
        <br />
        </div>
        <br />
        
        
        <div div className="buttons">
        <input type="file" onChange={handleMediaChange} />
        <button onClick={handleSubmit}>Post</button>
        <button onClick={closeModal} className='buttons'>Cancel</button>
        
        </div>
        
        
      </Modal>
    </div>
  );
}

export default PostSection;