// src/components/Prompt.js

import React, { useState } from 'react';
import axios from 'axios';

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
        <div>
            <input
                type="text"
                value={prompt}
                onChange={(e) => setPrompt(e.target.value)}
                placeholder="Enter your prompt"
            />
            <button onClick={handleSendPrompt}>Send Prompt</button>
            <div>
                <h3>Response:</h3>
                <p>{response}</p>
            </div>
        </div>
    );
};

export default Prompt;
