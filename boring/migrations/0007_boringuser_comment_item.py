# Generated by Django 3.2.4 on 2021-06-11 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boring', '0006_alter_game_iconclass2'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoringUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boring_coins', models.IntegerField(default=100)),
                ('boring_diamonds', models.IntegerField(default=10)),
                ('bio', models.TextField(blank=True)),
                ('level', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_coins', models.IntegerField(blank=True)),
                ('price_diamonds', models.IntegerField(blank=True)),
                ('description', models.TextField(max_length=150)),
                ('user', models.ManyToManyField(to='boring.BoringUser')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(max_length=250)),
                ('likes', models.IntegerField(default=0)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='boring.boringuser')),
            ],
        ),
    ]