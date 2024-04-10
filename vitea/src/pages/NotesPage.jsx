import React, { useState, useEffect } from 'react';

// This is the File component
const File = ({ file, deleteFile }) => (
  <div>
    <p>{file.name}</p>
    <button onClick={() => deleteFile(file.id)}>Delete</button>
  </div>
);

// This is the Files component
const Files = () => {
  const [files, setFiles] = useState([]);
  const [newFileName, setNewFileName] = useState('');

  useEffect(() => {
    fetch('/api/files')
      .then(response => response.json())
      .then(setFiles);
  }, []);

  const addFile = () => {
    const newFile = { id: Math.random(), name: newFileName };
    fetch('/api/files', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newFile),
    })
      .then(response => response.json())
      .then(file => setFiles([...files, file]));
  };

  const deleteFile = (id) => {
    fetch(`/api/files/${id}`, { method: 'DELETE' })
      .then(() => setFiles(files.filter(file => file.id !== id)));
  };

  return (
    <div>
      <input 
        type="text" 
        value={newFileName} 
        onChange={e => setNewFileName(e.target.value)} 
        placeholder="Enter new file name"
      />
      <button onClick={addFile}>Add File</button>
      {files.map(file => (
        <File key={file.id} file={file} deleteFile={deleteFile} />
      ))}
    </div>
  );
};

export default Files;
