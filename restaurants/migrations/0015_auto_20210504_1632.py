# Generated by Django 3.1.7 on 2021-05-04 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0014_auto_20210504_1628'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='openinghours',
            options={'ordering': ('weekday', 'from_hour'), 'verbose_name_plural': 'Opening Hours'},
        ),
    ]
