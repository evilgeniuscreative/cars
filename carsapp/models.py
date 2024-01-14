from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _

from django.db import models
from users import User
# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    cylinders = models.PositiveSmallIntegerField()  
    engine_type = models.CharField(max_length=100)
    displacement = models.CharField(max_length=100)
    displacement_type = models.CharField(  
        max_length=2,
        choices=[
            ("CI", _("Cubic Inches")),  
            ("L", _("Liters")),  
        ]
    )
    fuel_type = models.CharField(  
        max_length=10,
        choices=[
            ("GAS", _("Gas")),  
            ("DIESEL", _("Diesel")),  
            ("ELECTRIC", _("Electric")),  
            ("HYBRID", _("Hybrid")),  
            ("TWOSTROKE", _("Two Stroke Mix")),  
        ]
    )
    description = models.CharField(max_length=1500)
    color = models.CharField(max_length=100)
    customizations = models.CharField(max_length=1000)
    photos = ArrayField(
        models.ImageField(upload_to="car_images/")
    )

    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name="user", default=1)

    def __str__(self):
        return self.name
