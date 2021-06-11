# Generated by Django 3.2.4 on 2021-06-10 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boring', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='category',
            field=models.IntegerField(choices=[('1', 'Useless'), ('2', 'Creative'), ('3', 'Boring'), ('4', 'Frustration')], default=False),
        ),
    ]