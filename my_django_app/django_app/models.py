from django.db import models
from django.utils import timezone
# Create your models here.


class chaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('EL', 'ELACHI'),
        ('PL', 'PLAIN'),
    ]

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='chais/')
    dateAdded = models.DateTimeField(default=timezone.now())
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)

    def __Str__(self):
        return self.name
