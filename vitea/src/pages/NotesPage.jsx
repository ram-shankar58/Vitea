import React, { useState, useEffect } from 'react';
import NoteSharingComponent from './NoteSharingComponent';

const NotesPage = () => {
  const [notes, setNotes] = useState([]);
  const [selectedNote, setSelectedNote] = useState(null);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [branch, setBranch] = useState('');

  useEffect(() => {
    fetchNotes();
  }, []);

  const fetchNotes = async () => {
    const response = await fetch('/api/notes');
    const data = await response.json();
    setNotes(data);
  };

  const handleAddNote = async () => {
    const response = await fetch('/api/notes', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ title, description, branch }),
    });
    if (response.ok) {
      fetchNotes();
      setTitle('');
      setDescription('');
      setBranch('');
    }
  };

  const handleEditNote = async () => {
    const response = await fetch(`/api/notes/${selectedNote.id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ title, description, branch }),
    });
    if (response.ok) {
      fetchNotes();
      setSelectedNote(null);
      setTitle('');
      setDescription('');
      setBranch('');
    }
  };

  const handleDeleteNote = async (noteId) => {
    const response = await fetch(`/api/notes/${noteId}`, {
      method: 'DELETE',
    });
    if (response.ok) {
      fetchNotes();
      if (selectedNote && selectedNote.id === noteId) {
        setSelectedNote(null);
        setTitle('');
        setDescription('');
        setBranch('');
      }
    }
  };

  const handleNoteClick = (note) => {
    setSelectedNote(note);
    setTitle(note.title);
    setDescription(note.description);
    setBranch(note.branch);
  };

  return (
    <div>
      <h1>Notes</h1>

      <div>
        <h2>Create/Edit Note</h2>
        <input
          type="text"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <textarea
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        ></textarea>
        <input
          type="text"
          placeholder="Branch"
          value={branch}
          onChange={(e) => setBranch(e.target.value)}
        />
        {selectedNote ? (
          <button onClick={handleEditNote}>Save Note</button>
        ) : (
          <button onClick={handleAddNote}>Add Note</button>
        )}
      </div>

      <div>
        <h2>Notes List</h2>
        {notes.map((note) => (
          <div key={note.id}>
            <h3 onClick={() => handleNoteClick(note)}>{note.title}</h3>
            <button onClick={() => handleDeleteNote(note.id)}>Delete</button>
          </div>
        ))}
      </div>

      {selectedNote && (
        <div>
          <h2>Selected Note</h2>
          <h3>{selectedNote.title}</h3>
          <p>{selectedNote.description}</p>
          <p>Branch: {selectedNote.branch}</p>
        </div>
      )}

      <NoteSharingComponent />
    </div>
  );
};

export default NotesPage;
