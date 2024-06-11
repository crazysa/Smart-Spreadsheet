import React from 'react';
import FileUpload from './components/FileUpload';
import Prompt from './components/Prompt';
import './App.css';

function App() {
    return (
        <div className="App">
            <h1>SMART SpreadSheet (Beta)</h1>
            <FileUpload />
            <Prompt />
        </div>
    );
}

export default App;
