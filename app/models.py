from django.db import models

# Create your models here.


class dbmodel(models.Model):
    firstname = models.CharField(max_length=10)

    def __str__():
        return self.firstname
