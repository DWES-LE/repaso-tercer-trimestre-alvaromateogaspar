# Generated by Django 4.1.9 on 2023-06-16 14:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailcore", "0083_workflowcontenttype"),
        ("contacto", "0003_formfield_formpage_delete_contacto_formfield_page"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="FormPage",
            new_name="ContactPage",
        ),
    ]
