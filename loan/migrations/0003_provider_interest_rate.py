# Generated by Django 4.1.5 on 2023-08-01 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_user_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='interest_rate',
            field=models.IntegerField(null=True),
        ),
    ]
