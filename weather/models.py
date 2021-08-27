from django.db import models


class Weather(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    weather_object = models.JSONField(null=False)

    class Meta:
        verbose_name = "city"
        verbose_name_plural = "cities"

    def __str__(self):
        return f'{self.city}'
