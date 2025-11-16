💻 Online Code Execution Platform




This project is a simple Flask-based web application that allows users to execute code in multiple programming languages (Python, C, C++, Java, PHP, and NodeJS) using the JDoodle API.

✨ Features
Multi-Language Execution: Supports execution for several popular languages.

Web Interface: A basic, single-page interface for inputting code and viewing the output.

JDoodle API Integration: Uses the JDoodle API for backend code compilation and execution.

Program Display: An "All Programs" view to list and run pre-saved programs from programs.json (currently only supports running Python programs from this view).

⚙️ Project Structure
hh/
├── app.py                      # Main Flask application and JDoodle API integration logic
├── .env                        # Environment variables for JDoodle API keys
├── programs.json               # Placeholder for program metadata and source code (currently unused by app.py)
├── requirements.txt            # Python dependencies
├── templates/
│   ├── index.html              # Main code execution interface
│   ├── all_programs.html       # Interface for listing and running stored programs
│   ├── setup.bat               # Windows batch file for environment setup
│   └── composer.json           # PHP Composer dependencies list (example)
🛠️ Setup and Installation
Prerequisites
Python 3.x


Node.js & npm (optional, for package management and if developing the JS front-end) 


PHP & Composer (optional, for PHP dependency management) 

JDoodle API Credentials: You need a JDOODLE_CLIENTID and JDOODLE_CLIENTSECRET.

Steps
You can use the provided setup.bat file if you are on Windows, or follow the manual steps below.

Option 1: Using setup.bat (Windows)
Make sure you have Python, Node.js (for npm), and optionally PHP and Composer installed.

Run the batch file:

Bash

hh\templates\setup.bat
This script will:

Check for Python.

Create and activate a Python virtual environment (.venv).

Upgrade pip/setuptools/wheel.

Install Python packages from requirements.txt.

Install npm packages from package.json.

Run composer install if PHP/Composer is found.

Option 2: Manual Setup
Install Python Dependencies:

Bash

pip install -r requirements.txt
The required Python packages are Flask, python-dotenv, and requests.

Install Node Dependencies (Optional for this Flask app, but included in programs.json):

Bash

npm install
Configure API Keys:

Edit the .env file.

Replace the placeholder values with your actual JDoodle credentials:

Bash

JDOODLE_CLIENTID=cdcb924f002c45cd2654a59099cfc507 
JDOODLE_CLIENTSECRET=1ef61e37cf52007c84c402e768baa36af0f4fc606408f1b9d36b918293955816 
Running the Application
Start the Flask server:

Bash

python hh/app.py
The application will run in debug mode on port 5000.

Access the web interface in your browser at http://127.0.0.1:5000/.

📌 Dependencies
Python (requirements.txt)

Flask 


python-dotenv 


requests 

NodeJS (programs.json)
The project specifies numerous dependencies, often used in web development and utility tasks:

Web Frameworks: express, fastify

Databases: mongoose, mysql2, pg, sequelize

Security/Auth: bcrypt, jsonwebtoken, helmet, cors

Utilities: dotenv, axios, multer, socket.io, ejs, morgan, lodash, chalk, moment

Would you like me to elaborate on a specific part of the application, such as the JDoodle integration or the program execution flow?
