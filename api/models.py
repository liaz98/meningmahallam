from django.db import models

# Create your models here.


class Neighborhood(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    length = models.IntegerField(blank=True, null=True)
    square = models.FloatField()
    phone = models.CharField(max_length=100, blank=True, null=True)
    chairman = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Property(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, default="avatar.svg")
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name
