from django import forms
from .models import Soccerbot, LineFollow, IdeaGen, ChatGPT, RoboRace

# forms.py

from django import forms
from .models import Soccerbot, LineFollow, IdeaGen, ChatGPT, RoboRace

class BaseForm(forms.ModelForm):
    class Meta:
        widgets = {
            'team_Name': forms.TextInput(attrs={'class': 'custom-input'}),
            'team_Lead_Name': forms.TextInput(attrs={'class': 'custom-input'}),
            'team_Lead_StudentID': forms.TextInput(attrs={'class': 'custom-input'}),
            'team_Lead_Email': forms.TextInput(attrs={'class': 'custom-input'}),
            'team_Lead_Phone': forms.TextInput(attrs={'class': 'custom-input'}),
            'team_Lead_FacebookID': forms.TextInput(attrs={'class': 'custom-input'}),
            'member_2_name': forms.TextInput(attrs={'class': 'custom-input'}),
            'member_2_StudentID': forms.TextInput(attrs={'class': 'custom-input'}),
            'member_2_Email': forms.TextInput(attrs={'class': 'custom-input'}),
            'member_3_name': forms.TextInput(attrs={'class': 'custom-input'}),
            'member_3_StudentID': forms.TextInput(attrs={'class': 'custom-input'}),
            'member_3_Email': forms.TextInput(attrs={'class': 'custom-input'}),
            'member_4_name': forms.TextInput(attrs={'class': 'custom-input'}),
            'member_4_StudentID': forms.TextInput(attrs={'class': 'custom-input'}),
            'member_4_Email': forms.TextInput(attrs={'class': 'custom-input'}),
            'transactionID': forms.TextInput(attrs={'class': 'custom-input'}),
        }


class SoccerbotForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = Soccerbot
        exclude = ['payment_status', 'member_count']

class LineFollowForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = LineFollow
        exclude = ['payment_status', 'member_count']

class RoboRaceForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = RoboRace
        exclude = ['payment_status', 'member_count']

class IdeaGenForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = IdeaGen
        exclude = ['payment_status', 'member_count']

class ChatGPTForm(forms.ModelForm):
    class Meta:
        model = ChatGPT
        exclude = ['payment_status']
        widgets = {
            'teamName': forms.TextInput(attrs={'class': 'custom-input'}),
            'teamLeadName': forms.TextInput(attrs={'class': 'custom-input'}),
            'teamLeadStudentID': forms.TextInput(attrs={'class': 'custom-input'}),
            'transactionID': forms.TextInput(attrs={'class': 'custom-input'}),
            'team_Lead_Phone': forms.TextInput(attrs={'class': 'custom-input'}),
            # Add other fields with custom class as needed
        }
