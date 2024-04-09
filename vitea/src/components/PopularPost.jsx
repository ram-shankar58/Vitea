
import React, { useState } from 'react';
import './PopularPost.css'; // Import the CSS file

const PopularPost = () => {
    const [posts, setPosts] = useState([
        {
            id: 1,
            title: 'Top 10 JavaScript Frameworks',
            content: 'Check out this list of the top 10 JavaScript frameworks for web development.',
        },
        {
            id: 2,
            title: 'React vs Angular: Which one to choose?',
            content: 'Learn about the differences between React and Angular and decide which one is best for your project.',
        },
        {
            id: 3,
            title: 'Getting Started with Node.js',
            content: 'A beginner\'s guide to getting started with Node.js and building server-side applications.',
        }
    ]);

    const addPost = (newPost) => {
        setPosts([...posts, newPost]);
    };

    return (
        <div className="popular-post">
            <h2>Popular Posts</h2>
            <ul>
                {posts.map((post) => (
                    <li key={post.id} className="post">
                        <h3>{post.title}</h3>
                        <p>{post.content}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default PopularPost;