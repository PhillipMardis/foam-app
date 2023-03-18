from django.db import models
from django.contrib.auth.models import User, Group


# Create your models here.
class postModel(models.Model):
    CHOICES = (
        ("new", "new"),
        ("like-new", "like-new"),
        ("used-good", "used-good"),
        ("used", "used"),
    )
    user = models.ForeignKey(
        User,
        related_name="user_posts",
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    cond = models.CharField(choices=CHOICES, max_length=100)
    price = models.FloatField()


class buyModel(models.Model):
    CONDITION = (
        ("new", "new"),
        ("like-new", "like-new"),
        ("used-good", "used-good"),
        ("used", "used"),
    )

    PRICE = (
        ("$1-$30", "$1-$30"),
        ("$31-$50", "$31-$50"),
        ("$51-$100", "$51-$100"),
        ("+$100", "+$100"),
    )

    cond = models.CharField(choices=CONDITION, max_length=100, default=None)
    price = models.CharField(choices=PRICE, max_length=100, default=None)
