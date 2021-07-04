# Generated by Django 3.2.4 on 2021-07-04 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boring_website', '0011_answersubmission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answersubmission',
            name='submission',
        ),
        migrations.AddField(
            model_name='answersubmission',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers_submissions', to='boring_website.quizzsubmission'),
        ),
        migrations.AlterField(
            model_name='answersubmission',
            name='answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer_submissions', to='boring_website.answer'),
        ),
        migrations.CreateModel(
            name='QuestionSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions_submissions', to='boring_website.quizzsubmission')),
            ],
        ),
    ]
