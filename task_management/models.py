from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Task(models.Model):

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    assigned_to = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL, null=True, related_name='assigned_tasks')
    start_date = models.DateField()
    due_date = models.DateField()
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    location = models.CharField(max_length=255, null = True, blank=True)
    status = models.CharField(max_length=50, choices= STATUS_CHOICES)
    organizer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='organized_tasks')

    def __str__(self):
        return self.title