# Generated by Django 4.1.5 on 2023-08-02 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0006_alter_customer_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provider',
            name='interest_rate',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='max_amount',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='max_duration',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='min_amount',
        ),
        migrations.AddField(
            model_name='loan',
            name='interest_rate',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='loan',
            name='max_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='loan',
            name='max_duration',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='loan',
            name='min_amount',
            field=models.IntegerField(null=True),
        ),
    ]
