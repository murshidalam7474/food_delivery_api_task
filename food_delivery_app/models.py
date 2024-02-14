from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Item(models.Model):
    type = models.CharField(max_length=50)
    description = models.TextField()
    def __str__(self):
        return self.description

class Pricing(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    zone = models.CharField(max_length=50)
    base_distance_in_km = models.FloatField()
    km_price_perishable = models.FloatField()
    km_price_non_perishable = models.FloatField()
    fix_price = models.FloatField()
    def __str__(self):
        return f"{self.organization.name} - {self.item.description} - {self.zone}"
