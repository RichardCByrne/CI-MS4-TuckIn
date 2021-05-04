# Generated by Django 3.1.7 on 2021-05-04 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0013_openinghours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openinghours',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant'),
        ),
    ]