# Generated by Django 4.1.5 on 2023-08-05 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("loan", "0009_loan_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="loan",
            name="start_date",
        ),
        migrations.AddField(
            model_name="payment",
            name="loan",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="loan.loan"
            ),
        ),
        migrations.AlterField(
            model_name="loan",
            name="coustmer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="loan.customer",
            ),
        ),
        migrations.AlterField(
            model_name="loan",
            name="duration",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="loan",
            name="status",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="loan",
            name="total_amount",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
