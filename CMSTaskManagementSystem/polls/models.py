from django.conf import settings
from django.db import models


class Boards(models.Model):
    name = models.CharField(max_length=100)
    opendate = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Tasks(models.Model):
    fcolumn = models.ForeignKey('Boards', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    state = models.DecimalField(max_digits=1, decimal_places=0)
    assigneduser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, default=None)

class Asigments(models.Model):
    bid = models.ForeignKey('Boards', on_delete=models.CASCADE)
    uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)