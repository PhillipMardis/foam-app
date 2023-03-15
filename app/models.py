from django.db import models

# Create your models here.
class postModel(models.Model):
    CHOICES = (
        ("new", "new"),
        ("like-new", "like-new"),
        ("used-good", "used-good"),
        ("used", "used"),
    )
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    cond = models.CharField(choices=CHOICES, max_length=100)
    price = models.FloatField()


class buyModel(models.Model):
    CHOICES = (
        ("name", "name"),
        ("condition", "condition"),
        ("price", "price"),
    )

    browse_by = models.CharField(choices=CHOICES, max_length=100)
