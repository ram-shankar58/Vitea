import React, { useEffect, useState } from 'react';
import Navbar from '../components/Navbar';
import PopularPost from '../components/PopularPost';
import NoticeBoard from '../components/NoticeBoard';
import './HomePage.css'; // Import the CSS file
const HomePage = () => {
  const [showAdStrip, setShowAdStrip] = useState(true);

  useEffect(() => {
    const handleScroll = () => {
    //   const scrollPosition = window.scrollY;
    //   const adStripHeight = document.querySelector('.ad-strip').offsetHeight;

    //   if (scrollPosition > adStripHeight) {
    //     setShowAdStrip(false);
    //   } else {
    //     setShowAdStrip(true);
    //   }
    setShowAdStrip(false);
    };

    window.addEventListener('scroll', handleScroll);

    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  return (
    <>
      <Navbar />
      {showAdStrip && (
        <div className="ad-strip">
          <div className="ad">
            <p>HACKATHON 1!</p>
            <p>JOIN NOW!</p>
          </div>
          <div className="ad">
            <p>HACKATHON 2</p>
            <p>JOIN NOW!</p>
          </div>
          <div className="ad">
            <p>Advertisement 3</p>
          </div>
        </div>
      )}
      <NoticeBoard />
      <PopularPost />
    </>
  );
};

export default HomePage;
