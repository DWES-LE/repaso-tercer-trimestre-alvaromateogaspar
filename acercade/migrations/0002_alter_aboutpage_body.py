# Generated by Django 4.1.9 on 2023-06-18 08:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("acercade", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aboutpage",
            name="body",
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
