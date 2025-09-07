from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
