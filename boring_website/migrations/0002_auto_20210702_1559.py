# Generated by Django 3.2.4 on 2021-07-02 15:59

from django.db import migrations, models
from datetime import datetime

class Migration(migrations.Migration):

    dependencies = [
        ('boring_website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactbox',
            name='date_of_birth',
            field=models.DateTimeField(auto_now_add=True, default=datetime.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactbox',
            name='phone_number',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactbox',
            name='sur_name',
            field=models.CharField(default='Floyd', max_length=50),
            preserve_default=False,
        ),
    ]
