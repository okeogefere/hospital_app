# Generated by Django 4.2.7 on 2023-11-29 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_alter_appointments_special_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='special_id',
            field=models.CharField(default='efae5', editable=False, max_length=32, unique=True),
        ),
    ]
