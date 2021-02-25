from django.db import models

# Create your models here.

class ticket(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    #return string
    def _str_(self):
        return self.title

