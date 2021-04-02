# Generated by Django 3.1.7 on 2021-04-01 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0010_cuisine_icon_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='opening_hours',
            field=models.TextField(blank=True, default='Please enter opening hours', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='address_1',
            field=models.CharField(default='Please enter address 1', max_length=254),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='address_2',
            field=models.CharField(blank=True, default='Please enter address 2', max_length=254, null=True),
        ),
    ]
