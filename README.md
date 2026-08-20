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
