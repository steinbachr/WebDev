from django.db import models
from pickup_finder.constants import DataSourceConstants

class Game(models.Model):
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    normalized_location = models.CharField(max_length=200)
    data_source = models.CharField(max_length=1, choices=DataSourceConstants.choices_for_model())
    touch_datetime = models.DateTimeField()
    last_updated_datetime = models.DateTimeField()
    
