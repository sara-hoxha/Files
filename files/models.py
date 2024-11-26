from django.db import models

class File(models.Model):
    name = models.CharField(max_length=500)
    file_type = models.CharField(max_length=500)
    upload_timestamp = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name