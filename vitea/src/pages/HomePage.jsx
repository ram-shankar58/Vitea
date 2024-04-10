import React from 'react';
import Navbar from '../components/Navbar';
import PopularPost from '../components/PopularPost';
import NoticeBoard from '../components/NoticeBoard';
import './HomePage.css'; // Import the CSS file

const HomePage = () => {
    return (
        <>
            <Navbar />
            <div className="ad-strip">
                <div className="ad">
                    <p>HACKATHON 1!</p>
                    <a href="/LoginPage">Join Now!</a>
                </div>
                <div className="ad">
                <p>HACKATHON 2</p>
                <a href="/LoginPage">Join Now!</a>
                </div>
                <div className="ad">
                <p>XYZ CLUB</p>
                <a href="/LoginPage">Join Now!</a>
                </div>
            </div>
            <NoticeBoard />
            <PopularPost />
        </>
    );
};

export default HomePage;
