# Generated by Django 3.2.4 on 2021-09-19 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_delete_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='number_of_games',
            field=models.CharField(max_length=20),
        ),
    ]
