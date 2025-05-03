import React, { useState } from 'react';
import Students from './Students';
import Courses from './Courses';

function App() {
  const [view, setView] = useState('');
  const [nodeId, setNodeId] = useState('');

  const fetchNodeId = async () => {
    try {
      const res = await fetch('/students'); 
      const header = res.headers.get('X-Node-ID');
      setNodeId(header || 'Unknown');
    } catch (err) {
      console.error(err);
      setNodeId('Unavailable');
    }
  };

  const handleView = (v) => {
    setView(v);
    fetchNodeId();
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '2rem' }}>
      <h1>Frontend Load Balancer Demo</h1>
      <p>Served by: <strong>{nodeId}</strong></p>
      <button onClick={() => handleView('students')}>Students</button>
      <button onClick={() => handleView('courses')}>Courses</button>
      <div style={{ marginTop: '2rem' }}>
        {view === 'students' && <Students />}
        {view === 'courses' && <Courses />}
      </div>
    </div>
  );
}

export default App;
