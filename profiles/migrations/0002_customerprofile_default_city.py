# Generated by Django 3.1.7 on 2021-04-15 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprofile',
            name='default_city',
            field=models.CharField(default='Dublin', max_length=12),
        ),
    ]
