import React, { useState } from 'react';
import './PopularPost.css'; // Import the CSS file

const PopularPost = () => {
  const [posts, setPosts] = useState([
    {
      id: 1,
      title: 'General',
      content: 'Check out this list of the top 10 JavaScript frameworks for web development.',
    },
    {
      id: 2,
      title: 'Academic',
      content: 'Learn about the differences between React and Angular and decide which one is best for your project.',
    },
    {
      id: 3,
      title: 'Sports',
      content: 'A beginner\'s guide to getting started with Node.js and building server-side applications.',
    },
  ]);

  const addPost = (newPost) => {
    setPosts([...posts, newPost]);
  };

return (
    <div className="popular-post">
        <a href=""><h2>General</h2></a>
        <a href=""><h2>Academic</h2></a>
        <a><h2>Sports</h2></a>
        <a><h2>Entertainment</h2></a>
        <a href=""><h2>Science</h2></a>
        <a href=""><h2>Business</h2></a>
        <a><h2>Study Material</h2></a>
        <a><h2>Clubs</h2></a>
        <div className="box">
            <h2>Vit Help Center</h2>
            
            <p>Any problems, issues you are facing in VIT</p>
            <br />
            <button  onClick={() => window.open("https://vhelp.vit.ac.in/vitcc-help-center/", "_blank")}>
  Get Help
</button>



        </div>
    </div>
);
};

export default PopularPost;