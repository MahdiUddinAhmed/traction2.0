# Generated by Django 5.0.1 on 2024-02-03 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0011_alter_chatgpt_team_lead_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatgpt',
            name='team_Lead_Email',
            field=models.EmailField(default='None', max_length=254, unique=True),
        ),
    ]
