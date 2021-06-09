from django.db import models

# Create your models here.
class ElectricityDetail(models.Model):
    current = models.DecimalField(null=False, decimal_places=5, max_digits=50000)
    voltage = models.DecimalField(null=False, decimal_places=5, max_digits=50000)
    power = models.DecimalField(null=False, decimal_places=5, max_digits=50000)

    def __str__(self):
        return str(self.power)