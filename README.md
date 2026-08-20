📧 Bulk Email Automation System

A Django-based Bulk Email Automation System designed to process Excel files, validate and store records, and send bulk emails asynchronously using Celery and Redis.

The system separates email processing from the main Django request using background tasks, allowing the application to remain responsive while processing a large number of emails. OpenPyXL is used for Excel processing, Redis acts as the Celery message broker, and Docker provides a containerized environment for Redis.

🚀 Key Features
📂 Excel File Upload
Upload user/student records through Excel files.
Process Excel files using OpenPyXL without Pandas.
✅ Data Validation
Validate required fields such as name, age, and email.
Handle invalid records safely.
🔍 Duplicate Detection
Check uploaded records against existing database records.
Prevent duplicate data from being inserted.
💾 Database Storage
Store valid records in the Django database.
Maintain uploaded and processed record information.
📧 Bulk Email Sending
Send welcome emails to successfully uploaded users.
Use Django's email system with SMTP.
⚡ Asynchronous Email Processing
Use Celery to process emails in the background.
Prevent long-running email operations from blocking Django requests.
🔴 Redis Message Broker
Redis manages the queue between Django and Celery workers.
🐳 Docker Integration
Run Redis inside a Docker container.
Provides a consistent development environment.
📊 Upload History
Track uploaded files and processing results.
Maintain counts of total, uploaded, duplicate, and failed records.
📝 Remark Report
Generate an Excel report containing the processing status of each record.
Useful for identifying duplicate and failed records.
🎨 HTML Email Templates
Send dynamic and professional welcome emails using Django templates.
🏗️ System Architecture
                    ┌─────────────────┐
                    │      User       │
                    └────────┬────────┘
                             │
                             │ Upload Excel
                             ▼
                    ┌─────────────────┐
                    │     Django      │
                    │   Application   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    OpenPyXL     │
                    │ Excel Processing│
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   Validation &  │
                    │ Duplicate Check │
                    └──────┬─────┬────┘
                           │     │
                  Valid    │     │ Duplicate/Failed
                           ▼     ▼
                    ┌──────────┐ ┌──────────────┐
                    │ Database │ │ Remark Report│
                    └────┬─────┘ └──────────────┘
                         │
                         │ Create Email Task
                         ▼
                  ┌─────────────────┐
                  │     Celery      │
                  │  Background Job │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │      Redis      │
                  │  Message Broker │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Celery Worker   │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Django Email /  │
                  │      SMTP       │
                  └────────┬────────┘
                           │
                           ▼
                    📧 Recipient
🔄 Application Workflow
Step 1 — Upload Excel File

The user uploads an Excel file containing records such as:

Name        Age        Email
-----------------------------------------
Rahul       25         rahul@gmail.com
Amit        28         amit@gmail.com
Priya       24         priya@gmail.com
Step 2 — Read Excel Data

OpenPyXL reads the uploaded workbook and extracts the required fields.

workbook = load_workbook(uploaded_file)
sheet = workbook.active


for row in sheet.iter_rows(min_row=2, values_only=True):
    name, age, email = row
Step 3 — Validate Records

Each record is checked before insertion.

The system identifies:

Valid Record
Duplicate Record
Invalid/Failed Record
Step 4 — Save Valid Data

Valid records are stored in the Django database.

Step 5 — Create Background Email Tasks

For every successfully processed record, an email task is created:

send_welcome_email.delay(student.id)

Instead of sending the email immediately, the task is handed over to Celery.

Step 6 — Redis Queue

Redis acts as the message broker.

Django
   │
   │ Celery Task
   ▼
 Redis Queue
   │
   ▼
Celery Worker
Step 7 — Celery Worker

The Celery worker retrieves pending tasks from Redis and executes them independently from the Django request.

Step 8 — Send Email

The worker sends the welcome email through Django's email backend and SMTP server.

Celery Worker
      ↓
Django Email Backend
      ↓
SMTP Server
      ↓
Recipient
🛠️ Technology Stack
Technology	Purpose
Python	Core programming language
Django	Backend web framework
OpenPyXL	Excel reading and report generation
Celery	Asynchronous/background task processing
Redis	Celery message broker
Docker	Containerization for Redis
SMTP	Email delivery
MySQL	Database
HTML/CSS	Email templates
📁 Project Structure

A typical structure for the project:

bulk-email-project/
│
├── manage.py
│
├── project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── celery.py
│   └── wsgi.py
│
├── students/
│   ├── migrations/
│   ├── templates/
│   │   └── welcome.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tasks.py
│   ├── urls.py
│   └── views.py
│
├── media/
│   └── remarks/
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md

Adjust the folder names according to your actual repository structure.

⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/your-username/bulk-email-automation.git


cd bulk-email-automation
2. Create Virtual Environment
python -m venv venv
Windows
venv\Scripts\activate
Linux/macOS
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
🔴 4. Start Redis Using Docker

Make sure Docker Desktop is running.

If using Docker Compose:

docker compose up -d

Check running containers:

docker ps

You should see the Redis container running.

You can also verify Redis:

redis-cli ping

Expected response:

PONG
🗄️ 5. Configure Database

Update your Django database configuration in settings.py.

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
📧 6. Configure Email

Configure your SMTP credentials in environment variables.

Example:

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password

For Gmail, use an App Password rather than your normal Gmail password.

🗃️ 7. Run Migrations
python manage.py makemigrations
python manage.py migrate
👤 8. Create Superuser
python manage.py createsuperuser
▶️ 9. Start Django Server
python manage.py runserver

Open:

http://127.0.0.1:8000/
⚡ 10. Start Celery Worker

Open another terminal and activate your virtual environment.

Then run:

celery -A project worker --loglevel=info

Replace project with the actual Django project package name.

You should see the Celery worker connect to Redis.

transport: redis://localhost:6379/0
🔧 Celery Configuration

The project uses Redis as the Celery broker.

Example:

CELERY_BROKER_URL = "redis://localhost:6379/0"

Celery initialization:

from celery import Celery


app = Celery("project")


app.config_from_object(
    "django.conf:settings",
    namespace="CELERY"
)


app.autodiscover_tasks()
📩 Email Task

The email functionality is handled through a Celery task.

Example:

from celery import shared_task
from django.core.mail import EmailMultiAlternatives


@shared_task
def send_welcome_email(student_id):


    student = Student.objects.get(id=student_id)


    email = EmailMultiAlternatives(
        subject="Welcome!",
        body="Welcome to our platform.",
        from_email=settings.EMAIL_HOST_USER,
        to=[student.email],
    )


    email.send()

The task is triggered asynchronously:

send_welcome_email.delay(student.id)

This means Django doesn't need to wait for the email operation to finish.

📊 Upload & Processing Result

After processing an Excel file, the system tracks:

Total Records
     │
     ├── Successfully Uploaded
     │
     ├── Duplicate Records
     │
     └── Failed Records

Example:

Total Records : 100
Uploaded      : 85
Duplicate     : 10
Failed        : 5
📝 Remark Report

The system generates a remark Excel file using OpenPyXL.

Example:

Name	Age	Email	Status
Rahul	25	rahul@gmail.com	Uploaded
Amit	28	amit@gmail.com	Duplicate
Priya	24	priya@gmail.com	Failed

This provides a clear summary of how every uploaded record was processed.

🔐 Security Considerations

Sensitive configuration should not be committed to GitHub.

Use environment variables for:

SECRET_KEY
DATABASE_PASSWORD
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD

Add sensitive files to .gitignore:

.env
venv/
__pycache__/
*.pyc
db.sqlite3
media/
🧪 Testing the System

You can test the project with an Excel file containing:

New Records
John    25    john@gmail.com
David   28    david@gmail.com
Duplicate Records

Upload the same records again and verify that the system identifies them as duplicates.

Invalid Records

Test invalid:

Email addresses
Missing names
Invalid age values
Empty rows

Then verify that the generated remark report correctly identifies each record.

🧠 Key Concepts Demonstrated

This project demonstrates practical experience with:

Django MVC/MVT architecture
Django ORM
Excel file processing
Database operations
Data validation
Duplicate detection
Background task processing
Celery workers
Redis message queues
Docker containers
SMTP email integration
HTML email templates
File upload handling
Automated report generation
Asynchronous processing
💡 Why Celery + Redis?

Sending hundreds or thousands of emails directly inside a Django request can make the application slow and cause request timeouts.

Instead:

Without Celery


User
 ↓
Django
 ↓
Send 100 Emails
 ↓
Response

The user has to wait.

With Celery:

With Celery


User
 ↓
Django
 ↓
Create Tasks
 ↓
Immediate Response


Redis
 ↓
Celery Worker
 ↓
Send Emails

This improves the responsiveness of the application and separates email processing from the main web request.

📈 Future Enhancements

Possible improvements include:

 Email retry mechanism
 Failed email tracking
 Celery task monitoring with Flower
 Scheduled email campaigns
 Email delivery status tracking
 REST API integration using Django REST Framework
 User authentication and authorization
 Pagination for upload history
 Rate limiting for email delivery
 Multiple email templates
 Campaign management
 Docker Compose for the complete application
 Production deployment using AWS
👨‍💻 Learning Outcome

Through this project, I gained practical experience in designing a background job processing architecture using Django, Celery, and Redis. I also learned how to integrate Excel processing, database validation, asynchronous task execution, Docker-based services, and SMTP email delivery into a single backend application.

⭐ Project Highlights
📂 Excel Processing       → OpenPyXL
⚡ Background Tasks       → Celery
🔴 Message Broker         → Redis
🐳 Containerization       → Docker
📧 Email Delivery         → SMTP
💾 Data Storage           → MySQL
🌐 Backend                → Django
📝 Reports                → OpenPyXL
🔍 Validation             → Django Validation
📜 License

This project is created for learning and development purposes. You can add your preferred open-source license here, such as MIT.

👨‍💻 Author

Abhishek Singh Chauhan

Backend / Python Developer

Skills: Python • Django • REST API • Celery • Redis • Docker • MySQL • JavaScript • React
