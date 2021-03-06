# Generated by Django 3.2.4 on 2021-06-19 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boring', '0009_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='points_per_win',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='price_coins',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='price_diamonds',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
