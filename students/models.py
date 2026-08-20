from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
  



class UploadHistory(models.Model):

    file_name = models.CharField(
        max_length=255
    )

    file_hash = models.CharField(
        max_length=255,
        unique=True
    )

    total_records = models.IntegerField(
        default=0
    )

    uploaded_records = models.IntegerField(
        default=0
    )

    duplicate_records = models.IntegerField(
        default=0
    )

    failed_records = models.IntegerField(
        default=0
    )

    remark_file = models.FileField(
        upload_to="remarks/",
        null=True,
        blank=True
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.file_name