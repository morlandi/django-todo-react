from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(null=False, blank=True, max_length=120)
    description = models.TextField(null=False, blank=True)
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
