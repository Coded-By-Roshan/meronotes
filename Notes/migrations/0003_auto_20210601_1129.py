# Generated by Django 2.2.6 on 2021-06-01 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0002_feedback'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='feedback',
            new_name='Feeds',
        ),
    ]