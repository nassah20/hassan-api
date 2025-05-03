import React, { useEffect, useState } from 'react';

function Courses() {
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    fetch('/subjects')
      .then(res => res.json())
      .then(data => setCourses(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Software Engineering Subjects</h2>
      <ul>
        {courses.map((c, i) => (
          <li key={i}>{c.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default Courses;
