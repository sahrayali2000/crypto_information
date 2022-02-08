from django.db import models

# Create your models here.


class MarketInformation(models.Model):
    market_cap = models.CharField(max_length=1000)
    dominance = models.CharField(max_length=1000)
    volume = models.CharField(max_length=1000)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.market_cap} {self.dominance} {self.volume}'


class Asset(models.Model):
    key = models.CharField(max_length=20)
    change_percent = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(decimal_places=100, max_digits=500, null=True, blank=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.key
