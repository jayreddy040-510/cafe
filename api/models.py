from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(null=False, max_length=30)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
