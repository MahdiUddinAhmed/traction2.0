# Generated by Django 5.0.1 on 2024-02-02 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0008_linefollowmember_roboracemember_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatgpt',
            name='teamLeadPhone',
        ),
        migrations.AddField(
            model_name='chatgpt',
            name='transactionID',
            field=models.CharField(default='None', max_length=64),
        ),
        migrations.AddField(
            model_name='ideagen',
            name='transactionID',
            field=models.CharField(default='None', max_length=64),
        ),
        migrations.AddField(
            model_name='linefollow',
            name='transactionID',
            field=models.CharField(default='None', max_length=64),
        ),
        migrations.AddField(
            model_name='roborace',
            name='transactionID',
            field=models.CharField(default='None', max_length=64),
        ),
        migrations.AddField(
            model_name='soccerbot',
            name='transactionID',
            field=models.CharField(default='None', max_length=64),
        ),
    ]
