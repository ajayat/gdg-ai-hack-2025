import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import './NewCourse.css';

function NewCourse() {
  const [form, setForm] = useState({
    topic: '',
    date: '',
    objective: 'basic',
    style: 'strict',
  });

  useEffect(() => {
    document.title = 'Create New Course';
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Optionally POST to backend here
    // move to the quiz page
    window.location.href = '/quiz';
  };

  return (
    <div className="course-container">
      <div className="course-card">
        <h2>Create a New Course</h2>
        <form onSubmit={handleSubmit} className="course-form">
          <label>
            Topic:
            <input
              type="text"
              name="topic"
              value={form.topic}
              onChange={handleChange}
              required
            />
          </label>

          <label>
            Date:
            <input
              type="date"
              name="date"
              value={form.date}
              onChange={handleChange}
              required
            />
          </label>

          <label>
            Objective:
            <select name="objective" value={form.objective} onChange={handleChange}>
              <option value="basic">Basic</option>
              <option value="average">Average</option>
              <option value="best-grade">Best Grade</option>
            </select>
          </label>

          <label>
            Study Style:
            <select name="style" value={form.style} onChange={handleChange}>
              <option value="strict">Strict</option>
              <option value="chill">Chill</option>
              <option value="cheerful">Cheerful</option>
            </select>
          </label>

        <Link to="/coach">
            <button className="submit-btn">Create Course</button>
        </Link>
        </form>
      </div>
    </div>
  );
}

export default NewCourse;
