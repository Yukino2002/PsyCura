# Generated by Django 4.1.1 on 2022-09-25 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0005_remove_transaction_doctor_remove_transaction_patient_and_more'),
        ('Users', '0003_doctor_wallet_balance_patient_wallet_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='forum',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Services.forum'),
        ),
        migrations.AddField(
            model_name='sponsor',
            name='forum',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Services.forum'),
        ),
    ]
