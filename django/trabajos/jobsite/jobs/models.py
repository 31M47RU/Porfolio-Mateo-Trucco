from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=200, default="Trabajo")
    description = models.TextField(default="Descripcion")
    date_posted = models.DateField(auto_now_add=True)
    required_age = models.PositiveIntegerField(default="17")
    contact_number = models.CharField(max_length=20, default="1234567890")

    def __str__(self):
        return self.title
