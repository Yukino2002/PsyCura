# Generated by Django 4.1.1 on 2022-09-25 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0004_rename_forums_forum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='patient',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
