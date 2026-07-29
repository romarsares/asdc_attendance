from django.db import models
from core.models import BaseModel


class Region(BaseModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"Region {self.code} - {self.name}"


class Province(BaseModel):
    region = models.ForeignKey(Region, on_delete=models.PROTECT, related_name='provinces')
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Municipality(BaseModel):
    province = models.ForeignKey(Province, on_delete=models.PROTECT, related_name='municipalities')
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Barangay(BaseModel):
    municipality = models.ForeignKey(Municipality, on_delete=models.PROTECT, related_name='barangays')
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
