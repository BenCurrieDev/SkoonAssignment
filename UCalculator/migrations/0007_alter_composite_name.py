# Generated by Django 4.1.5 on 2023-02-04 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UCalculator', '0006_alter_material_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composite',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
