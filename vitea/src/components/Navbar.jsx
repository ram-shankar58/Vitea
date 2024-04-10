import React, { useState } from 'react';
import './Navbar.css'; // Import the CSS file
import ProfileImage from '../assets/profile.png'; // Replace with your default profile image path
import Logo from '../assets/vitea-logo.png';

const Navbar = () => {
  const [searchTerm, setSearchTerm] = useState('');

  const handleSearchChange = (event) => {
    setSearchTerm(event.target.value);
  };

  return (
    <nav className="nav-container">
      <img src={Logo} alt="Your App Logo" className="styled-logo" /> {/* Replace "logo.png" with your logo path */}
      <div className="search-bar-container">
        <input
          type="text"
          placeholder="Search"
          value={searchTerm}
          onChange={handleSearchChange}
          className="search-bar"
        />
      </div>
      <img src={ProfileImage} alt="Profile Picture" className="profile-icon" />
      
       {/* Replace "profile.png" with your default profile image path */}
      <ul className="nav-links">
        {/* ... your navigation links ... */}
      </ul>
      <button className='nii'>
   Logout
</button>
      
    </nav>


  );
};


export default Navbar;