from django.db import models

class VesselContact(models.Model):
    vessel_id = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    speed = models.FloatField()
    direction = models.CharField(max_length=50)
    vessel_type = models.CharField(max_length=100)
    threat_level = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
