# Generated by Django 3.2.4 on 2021-07-03 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boring_website', '0006_auto_20210703_1606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewelement',
            old_name='comments',
            new_name='comment',
        ),
    ]
