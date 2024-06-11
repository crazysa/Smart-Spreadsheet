// src/App.js

import React from 'react';
import FileUpload from './components/FileUpload';
import Prompt from './components/Prompt';

function App() {
    return (
        <div className="App">
            <h1>File Upload and Prompt Application</h1>
            <FileUpload />
            <Prompt />
        </div>
    );
}

export default App;
