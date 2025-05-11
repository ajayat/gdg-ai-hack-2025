import { useEffect } from 'react';
import { Link } from 'react-router-dom';
import './App.css';

function App() {
  useEffect(() => {
    document.title = "Braynr Coach Agent";
  }, []);

  return (
    <div className="hero">
      <h1 className="hero-title">Braynr Coach Agent</h1>
      <p className="hero-subtitle">
        Your personal AI-powered learning coach. Practice, reflect, and improve — all in one place.
      </p>
      <Link to="/new-course">
        <button className="hero-button">Start Learning</button>
      </Link>
    </div>
  );
}

export default App;