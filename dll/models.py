from django.db import models

class DB(models.Model):
    pp = models.CharField(max_length=100)
    po = models.CharField(max_length=100)

    def __str__(self):
        return self.pp