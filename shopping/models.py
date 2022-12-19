from django.db import models


# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=50)
    diskripsi = models.TextField()
    harga = models.IntegerField(null=True)
    
    def __str__(self):
        return self.name