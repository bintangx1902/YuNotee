# Generated by Django 3.0.3 on 2020-03-25 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yunote', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='url',
        ),
        migrations.AddField(
            model_name='note',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
