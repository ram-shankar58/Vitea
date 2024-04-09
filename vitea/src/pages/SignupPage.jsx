import React, { useState } from 'react';
import './SignupPage.css';
import logo from '../assets/vitea-logo.png';

const SignupPage = () => {
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [username, setUsername] = useState('');
    const [regNo, setRegNo] = useState('');
    const [branch, setBranch] = useState('');
    const [campus, setCampus] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSignup = (e) => {
        e.preventDefault();
        const data = {
            firstName,
            lastName,
            username,
            regNo,
            branch,
            campus,
            email,
            password
        };
    
        fetch('http://localhost:8000/login/create/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            // Handle the response data here
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    };

    return (
        <div className="container">
            <img src={logo} alt="Vitea Logo" className='logo'/>
            <form className="form" onSubmit={handleSignup}>
                <div className="form-row">
                    <div className="form-group">
                        <label>First Name:</label>
                        <input
                            type="text"
                            value={firstName}
                            onChange={(e) => setFirstName(e.target.value)}
                        />
                    </div>
                    <div className="form-group">
                        <label>Last Name:</label>
                        <input
                            type="text"
                            value={lastName}
                            onChange={(e) => setLastName(e.target.value)}
                        />
                    </div>
                </div>
                <div className="form-row">
                    <div className="form-group">
                        <label>Username:</label>
                        <input
                            type="text"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                        />
                    </div>
                    <div className="form-group">
                        <label>Registration Number:</label>
                        <input
                            type="text"
                            value={regNo}
                            onChange={(e) => setRegNo(e.target.value)}
                        />
                    </div>
                </div>
                <div className="form-row">
                    <div className="form-group">
                        <label>Branch:</label>
                        <input
                            type="text"
                            value={branch}
                            onChange={(e) => setBranch(e.target.value)}
                        />
                    </div>
                    <div className="form-group">
                        <label>Campus:</label>
                        <input
                            type="text"
                            value={campus}
                            onChange={(e) => setCampus(e.target.value)}
                        />
                    </div>
                </div>
                <div className="form-row">
                    <div className="form-group">
                        <label>Email:</label>
                        <input
                            type="email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                        />
                    </div>
                    <div className="form-group">
                        <label>Password:</label>
                        <input
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                    </div>
                </div>
                <div className="form-group">
                    <input type="submit" value="Signup" />
                </div>
            </form>
        </div>
    );
};

export default SignupPage;