#todo 
#create a containerised image 
#add db and user authentication and tracking


Things required to start the application:
    npm 
    python

to Run the frontend server:
    cd to frontend
    sudo npm install 
    sudo yarn add axios
    sudo npm start

to Run the backend server:
    cd backend
    install requirements.txt
    using vscode you can add below code to launch.json for debugging
        {
    "version": "0.2.0",
    "configurations": [
        
        {
            "name": "test",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/backend/chatbot/manage.py",
            "args": [
                "runserver"
            ],
            "django": true,
        },
       
    ]
}   
    can run the backedn interactivelu from Run and Debug tab in the left


change the 'OPENAI_API_KEY' in run_code.py file with your key