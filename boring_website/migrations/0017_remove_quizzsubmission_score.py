# Generated by Django 3.2.5 on 2021-07-05 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boring_website', '0016_quizzsubmission_final_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizzsubmission',
            name='score',
        ),
    ]