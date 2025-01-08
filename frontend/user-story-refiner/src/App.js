import React, { useState } from "react";
import axios from "axios";

function App() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [feedback, setFeedback] = useState("");
  const [refinedStory, setRefinedStory] = useState("");

  const handleSubmit = async () => {
    const feedbackList = feedback.split("\n").filter((item) => item.trim());
    const response = await axios.post("http://localhost:8000/refine_story", {
      title,
      description,
      feedback: feedbackList,
    });
    setRefinedStory(response.data.refined_story);
  };

  return (
    <div>
      <h1>User Story Refiner</h1>
      <div>
        <label>Title:</label>
        <input value={title} onChange={(e) => setTitle(e.target.value)} />
      </div>
      <div>
        <label>Description:</label>
        <textarea value={description} onChange={(e) => setDescription(e.target.value)} />
      </div>
      <div>
        <label>Feedback:</label>
        <textarea value={feedback} onChange={(e) => setFeedback(e.target.value)} placeholder="Enter feedback, one per line" />
      </div>
      <button onClick={handleSubmit}>Refine Story</button>
      <h2>Refined Story</h2>
      <pre>{refinedStory}</pre>
    </div>
  );
}

export default App;
