# Generated by Django 4.2.3 on 2023-07-20 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_choice_submission_question_choice_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='tries',
            field=models.IntegerField(default=0),
        ),
    ]
