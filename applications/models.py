from django.db import models
from django.conf import settings
from jobs.models import Job

User = settings.AUTH_USER_MODEL

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    resume = models.FileField(upload_to='resumes/')
    answers = models.TextField(blank=True)

    score = models.FloatField(null=True, blank=True)
    strengths = models.TextField(blank=True)
    weaknesses = models.TextField(blank=True)
    recommendations = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.job}"