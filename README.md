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


Main Workflow
User uploads an Excel file.
OpenPyXL reads the Excel data.
Django validates the records.
Duplicate records are identified.
Valid records are stored in the database.
Celery creates background email tasks.
Redis manages the task queue.
Celery Worker processes the tasks.
Welcome emails are sent using SMTP.
A remark report is generated for processed records.
Installation
1. Clone the Repository
