# Generated by Django 3.2.4 on 2021-06-22 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boring', '0013_auto_20210621_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='times_played',
            field=models.IntegerField(default=0),
        ),
    ]