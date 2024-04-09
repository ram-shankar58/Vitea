import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

const Post = () => {
    const [post, setPost] = useState(null);
    const { postNumber } = useParams();

    useEffect(() => {
        fetch(`http://localhost:8000/posts/${postNumber}`) // replace with your API endpoint
            .then(response => response.json())
            .then(data => setPost(data))
            .catch(error => console.error('Error:', error));
    }, [postNumber]);

    if (!post) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h1>{post.title}</h1>
            <p>{post.content}</p>
        </div>
    );
};

export default Post;