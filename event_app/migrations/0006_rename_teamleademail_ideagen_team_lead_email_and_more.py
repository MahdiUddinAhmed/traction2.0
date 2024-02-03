# Generated by Django 4.2.7 on 2024-02-01 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0005_ideagen_member_2_email_ideagen_member_2_studentid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ideagen',
            old_name='teamLeadEmail',
            new_name='team_Lead_Email',
        ),
        migrations.RenameField(
            model_name='ideagen',
            old_name='teamLeadName',
            new_name='team_Lead_Name',
        ),
        migrations.RenameField(
            model_name='ideagen',
            old_name='teamLeadPhone',
            new_name='team_Lead_Phone',
        ),
        migrations.RenameField(
            model_name='ideagen',
            old_name='teamLeadStudentID',
            new_name='team_Lead_StudentID',
        ),
        migrations.RenameField(
            model_name='ideagen',
            old_name='teamName',
            new_name='team_Name',
        ),
        migrations.RenameField(
            model_name='linefollow',
            old_name='teamLeadEmail',
            new_name='team_Lead_Email',
        ),
        migrations.RenameField(
            model_name='linefollow',
            old_name='teamLeadName',
            new_name='team_Lead_Name',
        ),
        migrations.RenameField(
            model_name='linefollow',
            old_name='teamLeadPhone',
            new_name='team_Lead_Phone',
        ),
        migrations.RenameField(
            model_name='linefollow',
            old_name='teamLeadStudentID',
            new_name='team_Lead_StudentID',
        ),
        migrations.RenameField(
            model_name='linefollow',
            old_name='teamName',
            new_name='team_Name',
        ),
        migrations.RenameField(
            model_name='roborace',
            old_name='teamLeadEmail',
            new_name='team_Lead_Email',
        ),
        migrations.RenameField(
            model_name='roborace',
            old_name='teamLeadName',
            new_name='team_Lead_Name',
        ),
        migrations.RenameField(
            model_name='roborace',
            old_name='teamLeadPhone',
            new_name='team_Lead_Phone',
        ),
        migrations.RenameField(
            model_name='roborace',
            old_name='teamLeadStudentID',
            new_name='team_Lead_StudentID',
        ),
        migrations.RenameField(
            model_name='roborace',
            old_name='teamName',
            new_name='team_Name',
        ),
        migrations.RenameField(
            model_name='soccerbot',
            old_name='teamLeadEmail',
            new_name='team_Lead_Email',
        ),
        migrations.RenameField(
            model_name='soccerbot',
            old_name='teamLeadName',
            new_name='team_Lead_Name',
        ),
        migrations.RenameField(
            model_name='soccerbot',
            old_name='teamLeadPhone',
            new_name='team_Lead_Phone',
        ),
        migrations.RenameField(
            model_name='soccerbot',
            old_name='teamLeadStudentID',
            new_name='team_Lead_StudentID',
        ),
        migrations.RenameField(
            model_name='soccerbot',
            old_name='teamName',
            new_name='team_Name',
        ),
        migrations.AddField(
            model_name='ideagen',
            name='team_Lead_FacebookID',
            field=models.URLField(default='Default Facebook ID', unique=True),
        ),
        migrations.AddField(
            model_name='linefollow',
            name='team_Lead_FacebookID',
            field=models.URLField(default='Default Facebook ID', unique=True),
        ),
        migrations.AddField(
            model_name='roborace',
            name='team_Lead_FacebookID',
            field=models.URLField(default='Default Facebook ID', unique=True),
        ),
        migrations.AddField(
            model_name='soccerbot',
            name='team_Lead_FacebookID',
            field=models.URLField(default='Default Facebook ID', unique=True),
        ),
    ]
