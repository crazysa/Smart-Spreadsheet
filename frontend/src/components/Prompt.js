import React, { useState } from 'react';
import axios from 'axios';
import './Prompt.css';

const Prompt = () => {
    const [prompt, setPrompt] = useState('');
    const [response, setResponse] = useState('');

    const handleSendPrompt = async () => {
        try {
            const res = await axios.post('http://localhost:5000/prompt', { prompt });
            setResponse(res.data.response);
        } catch (error) {
            console.error('Error sending prompt:', error);
        }
    };

    return (
        <div className="prompt-container">
            <h2>Send a Prompt</h2>
            <input
                type="text"
                className="prompt-input"
                value={prompt}
                onChange={(e) => setPrompt(e.target.value)}
                placeholder="Enter your prompt"
            />
            <button className="prompt-button" onClick={handleSendPrompt}>Send Prompt</button>
            {response && (
                <div className="prompt-response">
                    <h3>Response:</h3>
                    <p>{response}</p>
                </div>
            )}
        </div>
    );
};

export default Prompt;
