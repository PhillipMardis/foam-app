# Generated by Django 4.1.5 on 2023-03-16 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_alter_buymodel_browse_by"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="buymodel",
            name="browse_by",
        ),
        migrations.AddField(
            model_name="buymodel",
            name="cond",
            field=models.CharField(
                choices=[
                    ("new", "new"),
                    ("like-new", "like-new"),
                    ("used-good", "used-good"),
                    ("used", "used"),
                ],
                default=None,
                max_length=100,
            ),
        ),
        migrations.AddField(
            model_name="buymodel",
            name="price",
            field=models.CharField(
                choices=[
                    ("$1-$30", "$1-$30"),
                    ("$31-$50", "$31-$50"),
                    ("$51-$100", "$51-$100"),
                    ("+$100", "+$100"),
                ],
                default=None,
                max_length=100,
            ),
        ),
    ]
