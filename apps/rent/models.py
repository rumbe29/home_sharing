from django.db import models


class Image(models.Model):
    Image = models.ImageField()


class Apartment(models.Model):
    description = models.TextField(blank=True, null=True, verbose_name="Opisanie")
    address = models.CharField(max_length=150, verbose_name="adres", null=True)
    cost = models.FloatField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
