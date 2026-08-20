from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from .models import Student


@shared_task
def send_welcome_email(student_id):
    student = Student.objects.get(id=student_id)

    html_content = render_to_string(
        "welcome.html",
        {"student": student}
    )

    email_message = EmailMultiAlternatives(
        subject="Welcome Email",
        body="Your data has been successfully added.",
        from_email=settings.EMAIL_HOST_USER,
        to=[student.email],
    )

    email_message.attach_alternative(html_content, "text/html")
    email_message.send(fail_silently=False)

    return f"Email sent successfully to {student.email}"