# Generated by Django 3.1.7 on 2021-05-17 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='isCompleted',
            field=models.BooleanField(default=False),
        ),
    ]
