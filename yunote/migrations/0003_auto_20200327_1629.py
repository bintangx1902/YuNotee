# Generated by Django 3.0.3 on 2020-03-27 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yunote', '0002_auto_20200325_2202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='tittle',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='note',
            name='note',
        ),
        migrations.AddField(
            model_name='note',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
