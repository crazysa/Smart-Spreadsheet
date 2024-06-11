import React, { useState } from 'react';
import axios from 'axios';
import './FileUpload.css';

const FileUpload = () => {
    const [files, setFiles] = useState([]);

    const handleFileChange = (event) => {
        setFiles(event.target.files);
    };

    const handleUpload = async () => {
        const formData = new FormData();
        for (let i = 0; i < files.length; i++) {
            formData.append('files', files[i]);
        }

        try {
            const response = await axios.post('http://127.0.0.1:8000/api/upload', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            console.log(response.data);
        } catch (error) {
            console.error('Error uploading files:', error);
        }
    };

    return (
        <div className="file-upload-container">
            <h2>Upload Excel Files</h2>
            <input 
                type="file" 
                id="file-upload" 
                multiple 
                onChange={handleFileChange} 
            />
            <label htmlFor="file-upload" className="file-upload-label">Choose Files</label>
            <button className="upload-button" onClick={handleUpload}>Upload</button>
        </div>
    );
};

export default FileUpload;
