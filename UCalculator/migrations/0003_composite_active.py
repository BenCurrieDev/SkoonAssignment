# Generated by Django 4.1.5 on 2023-01-30 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UCalculator', '0002_component_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='composite',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
