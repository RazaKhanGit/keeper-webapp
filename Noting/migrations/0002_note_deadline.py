# Generated by Django 3.1.3 on 2020-11-29 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Noting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='deadline',
            field=models.DateTimeField(default=0),
        ),
    ]
