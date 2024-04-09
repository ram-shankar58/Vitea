import React, { useState } from 'react';
import './SignupPage.css';
import logo from '../assets/vitea-logo.png';

const SignupPage = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSignup = (e) => {
        e.preventDefault();
        // Add your signup logic here
    };

    return (
        <div className="container">
            <img src={logo} alt="Vitea Logo" className='logo'/>
            <form className="form" onSubmit={handleSignup}>
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
                <div className="form-group">
                    <input type="submit" value="Signup" />
                </div>
            </form>
        </div>
    );
};

export default SignupPage;