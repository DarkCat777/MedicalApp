from django.db import models


# Create your models here.
class Patient(models.Model):
    full_name = models.CharField(max_length=255, null=False, blank=False)
    birth_date = models.DateField(blank=False, null=False, auto_now=False, auto_created=False, auto_now_add=False)
    height = models.FloatField(blank=False, null=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    location_latitude = models.FloatField(null=False, blank=False)
    location_longitude = models.FloatField(null=False, blank=False)

    def __str__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items() if item[0][0] != '_')
        )
