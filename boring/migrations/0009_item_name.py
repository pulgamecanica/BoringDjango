# Generated by Django 3.2.4 on 2021-06-19 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boring', '0008_auto_20210611_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(default='Boring Item', max_length=50),
        ),
    ]