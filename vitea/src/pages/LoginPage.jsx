import React, { useState } from 'react';
import './LoginPage.css';
import logo from '../assets/vitea-logo.png';

const LoginPage = () => {
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
        // Add your login logic here
    };

    return (
        <div className="container">
            <img src={logo} alt="Vitea Logo" className='logo'/>
            <form className="login-form" onSubmit={handleSubmit}>
                <label>
                    Email:
                    <input type="email" value={username} onChange={handleUsernameChange} className="login-form input" />
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