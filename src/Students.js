import React, { useEffect, useState } from 'react';

function Students() {
  const [students, setStudents] = useState([]);

  useEffect(() => {
    fetch('/students')
      .then(res => res.json())
      .then(data => setStudents(data.slice(0, 10)))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Students</h2>
      <ul>
        {students.map((s, i) => (
          <li key={i}>{s.name} — {s.program}</li>
        ))}
      </ul>
    </div>
  );
}

export default Students;
