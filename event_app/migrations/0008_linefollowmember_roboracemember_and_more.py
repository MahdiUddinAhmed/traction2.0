# Generated by Django 4.2.7 on 2024-02-01 16:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0007_chatgptmemebers_soccerbotmember'),
    ]

    operations = [
        migrations.CreateModel(
            name='lineFollowMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_ID', models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator(regex='^[0-9]{8}$')])),
            ],
        ),
        migrations.CreateModel(
            name='RoboRaceMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_ID', models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator(regex='^[0-9]{8}$')])),
            ],
        ),
        migrations.RenameModel(
            old_name='ChatGPTMemebers',
            new_name='IdeaGenMember',
        ),
    ]
