import React, { useState } from 'react';
import './LoginPage.css';
import logo from '../assets/vitea-logo.png';

const LoginPage = () => {
    const useHistory = useHistory();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleUsernameChange = (e) => {
        setUsername(e.target.value);
    };

    const handlePasswordChange = (e) => {
        setPassword(e.target.value);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
    
        const data = {
            username,
            password
        };
    
        fetch('http://localhost:8000/login/token/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            // Store the authentication token in local storage
            localStorage.setItem('authToken', data.token);
            history.push('/home');
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    };

    return (
        <div className="container">
            <img src={logo} alt="Vitea Logo" className='logo'/>
            <form className="login-form" onSubmit={handleSubmit}>
                <label>
                    Username:
                    <input type="text" value={username} onChange={handleUsernameChange} className="login-form input" />
                </label>
                <br />
                <label>
                    Password:
                    <input type="password" value={password} onChange={handlePasswordChange} className="login-form input" />
                </label>
                <br />
                <button type="submit" className="login-form button">Login</button>
            </form>
        </div>
    );
};

export default LoginPage;