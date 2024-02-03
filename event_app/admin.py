from django.contrib import admin
from .models import Soccerbot, LineFollow, RoboRace, IdeaGen, ChatGPT, SoccerbotMember, lineFollowMember, IdeaGenMember, RoboRaceMember


class SoccerbotAdmin(admin.ModelAdmin):
    list_display = ['team_Name', 'team_Lead_Name',
                    'team_Lead_Email', 'transactionID', 'payment_status']


class LineFollowAdmin(admin.ModelAdmin):
    list_display = ['team_Name', 'team_Lead_Name',
                    'team_Lead_Email', 'transactionID', 'payment_status']


class ProjectShowCaseAdmin(admin.ModelAdmin):
    list_display = ['team_Name', 'team_Lead_Name',
                    'team_Lead_Email', 'transactionID', 'payment_status']


class IdeaGenAdmin(admin.ModelAdmin):
    list_display = ['team_Name', 'team_Lead_Name',
                    'team_Lead_Email', 'transactionID', 'payment_status']


class ChatGPTAdmin(admin.ModelAdmin):
    list_display = ['teamLeadStudentID', 'teamLeadName',
                    'team_Lead_Phone', 'transactionID', 'payment_status']


admin.site.register(Soccerbot, SoccerbotAdmin)
admin.site.register(LineFollow, LineFollowAdmin)
admin.site.register(RoboRace, ProjectShowCaseAdmin)
admin.site.register(IdeaGen, IdeaGenAdmin)
admin.site.register(ChatGPT, ChatGPTAdmin)
admin.site.register(SoccerbotMember)
admin.site.register(lineFollowMember)
admin.site.register(IdeaGenMember)
admin.site.register(RoboRaceMember)

admin.site.site_title = "Techspectra Admin Panel"
admin.site.site_header = "Techspectra Admin"
admin.site.index_title = "Site administration"
