# Generated by Django 4.2.2 on 2023-06-06 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_remove_blogpage_intro_blogpage_enlace_redes_sociales_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpage",
            name="nombre",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
