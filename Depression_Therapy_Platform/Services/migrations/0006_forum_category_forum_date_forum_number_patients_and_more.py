# Generated by Django 4.1.1 on 2022-09-25 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0005_remove_transaction_doctor_remove_transaction_patient_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='forum',
            name='date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='forum',
            name='number_patients',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Sessions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=None)),
                ('time', models.TimeField(default=None)),
                ('report', models.CharField(blank=True, max_length=100, null=True)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Services.forum')),
            ],
        ),
    ]