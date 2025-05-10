import { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [input, setInput] = useState('');
  const [response, setResponse] = useState('');

  useEffect(() => {
    document.title = "Braynr Coach";
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await axios.post('http://localhost:8000/chat', { message: input });
    setResponse(res.data.response);
  };

  return (
    <div className="container">
      <h1>AI Agent Chat</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a message"
        />
        <button type="submit">Send</button>
      </form>
      <p><strong>Response:</strong> {response}</p>
    </div>
  );
}

export default App;
