// frontend/src/Coach.jsx
import { useState, useEffect } from 'react';
import axios from 'axios';
import './Coach.css';

function Coach() {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [score, setScore] = useState(null);
  const [correctAnswer, setCorrectAnswer] = useState('');


  const fetchQuestion = async () => {
    try {
      const res = await axios.get('http://localhost:8000/question');
      setQuestion(res.data.question);
      setAnswer('');
      setScore(null);
    } catch (err) {
      setQuestion("⚠️ Unable to load question. Please try again later.");
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await axios.post('http://localhost:8000/score', {
      question,
      answer,
    });
    setScore(res.data.score);
    setCorrectAnswer(res.data.answer);
  };

  const sendFeedback = async (value) => {
    await axios.post('http://localhost:8000/feedback', {
      question,
      feedback: value,
    });
  };


  useEffect(() => {
    document.title = "Braynr Coach - Learning Session";
    fetchQuestion();
  }, []);

  return (
    <div className="coach-container">
      <div className="coach-card">
        <h2 className="coach-title">AI Braynr Coach</h2>
        <form onSubmit={handleSubmit} className="coach-form">
          <div className="question-box">
            <strong>Question:</strong>
            <p>{question}</p>
          </div>
          <label>
            Your Answer:
            <textarea
              rows="5"
              value={answer}
              onChange={(e) => setAnswer(e.target.value)}
              placeholder="Write your answer"
              required
            />
          </label>
          <button type="submit" className="submit-btn">Submit Answer</button>
          <div className="feedback-buttons">
            <button type="button" className="like-btn" onClick={() => sendFeedback(1)}>
              👍 Like
            </button>
            <button type="button" className="dislike-btn" onClick={() => sendFeedback(0)}>
              👎 Dislike
            </button>
          </div>
        </form>

      {score !== null && (
        <>
          <div className="score-box">
            <strong>Score:</strong> {score}/100
          </div>
          <div className="correct-answer-box">
            <strong>Correct Answer:</strong> {correctAnswer}
          </div>
          <button onClick={fetchQuestion} className="submit-btn">
            Next Question
          </button>
        </>
      )}
      </div>
    </div>
  );
}

export default Coach;
