# django-task
A simple Django-based Q&A web application inspired by Quora.
Users can sign up, log in, post questions, answer them, like answers, and log out.
# Features
a)User authentication (Sign up / Login / Logout)
b)Post questions
c)View all questions
d)Answer questions
e)Like answers
f)Execution time logging for each view
g)Test cases included 

## Clone the Repository
git clone https://github.com/1jb12me030/django-task.git
cd django-task
## Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate  # On Windows
# Install Dependencies
pip install -r requirements.txt
# Apply Migrations
python manage.py makemigrations
python manage.py migrate
# Create a Superuser
python manage.py createsuperuser
# Run the Server
python manage.py runserver
# use this : http://127.0.0.1:8000 to start using the app

## Run Tests (with Execution Time)
python manage.py test

## API Endpoints
# Method	         URL	                                           Description

GET	             /	                                          Home -All Questions
GET	          /signup/	                                      Register new user
GET	          /login/	                                        Login user
POST	        /logout/	                                      Logout(via form)
GET/POST	    /ask/	                                          Post a new question
GET/POST	    /question/<int:pk>/	                            Answer a question
POST	        /like/<int:answer_id>/	                        Like an answer

## Logging Setup
Logs are stored in the /logs/ directory.
Execution time of views is logged in logs/execution_time.log.

## Project Structure
quora_task/
│
├── testapp/                     # Core Django app
│   ├── views.py                 # All views (login, logout, post question, etc.)
│   ├── models.py                # Models for Question and Answer
│   ├── urls.py                  # URL routes for testapp
│   ├── tests.py                 #  Unit tests for all key views and APIs (login, logout, question, like, etc.)
│
├── templates/                   # HTML templates for login, signup, home, question detail, etc.
│
├── logs/                        # Execution time & API logs
│   └── django.log               # Log file auto-generated via logging config in settings.py
│
├── .gitignore                   #  Git ignore file ( venv/, *.pyc, __pycache__, db.sqlite3, etc.)
│
├── manage.py                    # Django’s command-line utility
└── requirements.txt             # All required Python packages

************************************************* Thank you for checking out this project!  *******************************************************


