# Generated by Django 4.1.4 on 2023-03-14 08:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note_app', '0002_notemodel_note_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notemodel',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 14, 8, 35, 21, 280790, tzinfo=datetime.timezone.utc)),
        ),
    ]
