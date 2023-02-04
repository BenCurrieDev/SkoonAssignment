# Generated by Django 4.1.5 on 2023-02-04 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('K_value', models.FloatField()),
                ('color', models.CharField(default='grey', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Composite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depth', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('composite', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UCalculator.composite')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UCalculator.material')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
