# Generated by Django 4.1.5 on 2023-08-14 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0010_remove_loan_start_date_payment_loan_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='total_fees',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='loan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='loan.loan'),
        ),
    ]
