# Generated by Django 3.2.4 on 2021-06-11 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boring', '0005_auto_20210611_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='iconClass2',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
    ]
