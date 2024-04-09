import React, { useState } from 'react';
import './NoticeBoard.css'; // Import the CSS file

const NoticeBoard = () => {
  const [notices, setNotices] = useState([
    {
      id: 1,
      title: 'Important Update!',
      content: 'There is a new update available for the application. Please download and install it for the latest features.',
    },
    {
      id: 2,
      title: 'Reminder: Meeting Today',
      content: 'Don\'t forget about the team meeting today at 2 PM. We will be discussing the upcoming project launch.',
    },
    {
      id: 3,
      title: 'Welcome New Team Members!',
      content: 'We have two new team members joining us this week. Please welcome them and help them get settled in.',
    }
  ]);

  const addNotice = (newNotice) => {
    setNotices([...notices, newNotice]);
  };

  return (
    <div className="notice-board">
      <h2>Notice Board</h2>
      <ul>
        {notices.map((notice) => (
          <li key={notice.id} className="notice">
            <h3>{notice.title}</h3>
            <p>{notice.content}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default NoticeBoard;