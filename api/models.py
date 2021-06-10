from django.db import models

# Create your models here.
class ElectricityDetail(models.Model):
    current = models.DecimalField(null=False, decimal_places=4, max_digits=1000)
    voltage = models.DecimalField(null=False, decimal_places=4, max_digits=1000)
    power = models.DecimalField(null=False, decimal_places=4, max_digits=1000)
    date_stamp=models.DateField(auto_now_add=True)
    time_stamp=models.TimeField(auto_now_add=True)

    def __str__(self):
        return str(self.power)+" "+ str(self.date_stamp)+" "+str(self.time_stamp)