from django.db import models


class ViewersCount(models.Model):
    path = models.CharField(max_length=500,blank=True,null = True)
    views = models.IntegerField(default=0,blank=True,null = True)
    ipaddress = models.CharField(max_length=500,blank=True,null = True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.path

