# Bulk Email Automation System

A Django-based application that allows users to upload Excel files, validate and store data in the database, and send bulk welcome emails asynchronously using Celery and Redis.

## Features

- Upload data through Excel files
- Read Excel files using OpenPyXL
- Validate uploaded records
- Detect duplicate records
- Store valid records in the database
- Send bulk welcome emails
- Background email processing using Celery
- Redis as Celery message broker
- Redis running through Docker
- Generate Excel remark reports
- Maintain upload history
- Send emails using SMTP

## Tech Stack

- Python
- Django
- MySQL
- OpenPyXL
- Celery
- Redis
- Docker
- SMTP
- HTML/CSS

## How It Works

```text
Excel Upload
     ↓
Django
     ↓
Validation & Duplicate Check
     ↓
Database
     ↓
Celery Task
     ↓
Redis
     ↓
Celery Worker
     ↓
SMTP
     ↓
Email

Project Workflow
1. Excel Upload

The user uploads an Excel file containing user information such as:

Name        Age        Email
Rahul       25         rahul@gmail.com
Amit        28         amit@gmail.com
Priya       24         priya@gmail.com
2. Excel Processing

OpenPyXL is used to read the uploaded Excel file and extract the required data.

3. Data Validation

The system validates the uploaded records before storing them in the database.

4. Duplicate Check

The system checks whether the record already exists in the database.

Duplicate records are not inserted again.

5. Database Storage

Valid records are stored in the MySQL database using Django ORM.

6. Background Email Task

After successfully storing the data, a Celery task is created for sending the welcome email.

send_welcome_email.delay(student.id)
7. Redis

Redis works as the message broker between Django and Celery.

Django
   ↓
Celery Task
   ↓
Redis
   ↓
Celery Worker
8. Celery Worker

The Celery worker receives the task from Redis and processes the email in the background.

9. Email Sending

The email is sent using Django's email functionality and SMTP.

Celery Worker
     ↓
Django Email
     ↓
SMTP Server
     ↓
User Email
10. Remark Report

The system generates an Excel remark report containing the status of processed records.

Example:

Name       Age    Email              Status
------------------------------------------------
Rahul      25     rahul@gmail.com    Uploaded
Amit       28     amit@gmail.com      Duplicate
Priya      24     priya@gmail.com    Failed
Upload History

The system maintains upload history and tracks:

Total Records
Uploaded Records
Duplicate Records
Failed Records
Remark Report

Example:

Total     : 100
Uploaded  : 85
Duplicate : 10
Failed    : 5
Celery Configuration

Celery uses Redis as the message broker.

CELERY_BROKER_URL = "redis://localhost:6379/0"
Docker

Redis is run using Docker.

Start Redis using:

docker compose up -d

Check running containers:

docker ps
Installation
1. Clone the Repository
git clone https://github.com/your-username/bulk-email-automation.git


cd bulk-email-automation
2. Create Virtual Environment
python -m venv venv

For Windows:

venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure Database

Update your database configuration in settings.py.

Example:

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "bulk_email_db",
        "USER": "root",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
5. Configure Email

Add your SMTP configuration.

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "your_email@gmail.com"
EMAIL_HOST_PASSWORD = "your_app_password"
6. Run Migrations
python manage.py makemigrations
python manage.py migrate
7. Start Redis

Make sure Docker is running and execute:

docker compose up -d
8. Start Django Server
python manage.py runserver
9. Start Celery Worker

Open another terminal and run:

celery -A project worker --loglevel=info

Replace project with your actual Django project name.

Requirements

Example requirements.txt:

Django
celery
redis
openpyxl
mysqlclient
Security

Do not upload sensitive information such as:

.env
Email Password
Database Password
Django SECRET_KEY

Add them to .gitignore.

.env
venv/
__pycache__/
*.pyc
media/
Project Structure
Bulk-Email-Automation/
│
├── manage.py
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   ├── celery.py
│   └── wsgi.py
│
├── students/
│   ├── migrations/
│   ├── templates/
│   │   └── welcome.html
│   ├── models.py
│   ├── views.py
│   ├── tasks.py
│   ├── urls.py
│   └── admin.py
│
├── media/
│   └── remarks/
│
├── requirements.txt
├── docker-compose.yml
├── .gitignore
└── README.md
Key Concepts Used
Django ORM
Django File Upload
Excel Processing
Data Validation
Duplicate Detection
Celery Background Tasks
Redis Message Broker
Docker
SMTP Email
Database Management
Excel Report Generation
Asynchronous Processing
Future Improvements
Email retry mechanism
Celery Flower for task monitoring
Email delivery tracking
Scheduled email sending
Email campaign management
Django REST Framework API
User authentication
Pagination
Production deployment
Author

Abhishek Singh Chauhan

Python / Django Developer

License

This project is created for learning and development purposes.
