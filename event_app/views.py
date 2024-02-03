from django.shortcuts import render, redirect
from .forms import SoccerbotForm, LineFollowForm, RoboRaceForm, IdeaGenForm, ChatGPTForm
from .models import SoccerbotMember, lineFollowMember, RoboRaceMember, IdeaGenMember
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib import messages

def home(request):
    return render(request, "event_app/home.html", {})

def segments(request):
    return render(request, "event_app/segments.html", {})

def registration_complete(request):
    return render(request, 'event_app/registration_complete.html')

def web_dev_team(request):
    return render(request, 'event_app/web_dev_team.html', {})


def soccerbot_registration(request):
    if request.method == 'POST':
        form = SoccerbotForm(request.POST)
        if form.is_valid():
            soccerbot_instance = form.save()  
            student_ids = [soccerbot_instance.team_Lead_StudentID]

            # Handling team lead's student ID
            try:
                SoccerbotMember.objects.create(student_ID=soccerbot_instance.team_Lead_StudentID)
            except IntegrityError:
                messages.error(request, f"Team Lead's Student ID {soccerbot_instance.team_Lead_StudentID} already exists.")

            # Handling member student IDs
            for i in range(2, 5):  # Loop through member fields
                member_id_field = f'member_{i}_StudentID'
                member_id = form.cleaned_data.get(member_id_field)
                if member_id:  # If member ID is not empty
                    try:
                        SoccerbotMember.objects.create(student_ID=member_id)
                    except IntegrityError:
                        messages.error(request, f"Student ID {member_id} already exists.")

            messages.success(request, "Registration successful.")
            return redirect('reg-complete')  # Update this line
        else:
            messages.error(request, "One of the entered data may not be correct or One of the Student IDs already exists. A member cannot be part of two teams. If not, please contact us!")
    else:
        form = SoccerbotForm()
    return render(request, 'event_app/soccer.html', {'form': form})


def linefollow_registration(request):
    if request.method == "POST":
        form = LineFollowForm(request.POST)
        if form.is_valid():
            lineFollow_instance = form.save()  
            student_ids = [lineFollow_instance.team_Lead_StudentID]

            # Handling team lead's student ID
            try:
                lineFollowMember.objects.create(student_ID=lineFollow_instance.team_Lead_StudentID)
            except IntegrityError:
                messages.error(request, f"Team Lead's Student ID {lineFollow_instance.team_Lead_StudentID} already exists.")

            # Handling member student IDs
            for i in range(2, 5):  # Loop through member fields
                member_id_field = f'member_{i}_StudentID'
                member_id = form.cleaned_data.get(member_id_field)
                if member_id:  # If member ID is not empty
                    try:
                        lineFollowMember.objects.create(student_ID=member_id)
                    except IntegrityError:
                        messages.error(request, f"Student ID {member_id} already exists.")

            messages.success(request, "Registration successful.")
            return redirect('reg-complete')  # Update this line
        else:
            messages.error(request, "One of the entered data may not be correct or One of the Student IDs already exists. A member cannot be part of two teams. If not, please contact us!")
    else:
        form = LineFollowForm()
    return render(request, 'event_app/lfr.html', {'form': form})


from django.db import IntegrityError
from django.contrib import messages

def chatbot_registration(request):
    if request.method == "POST":
        form = ChatGPTForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("reg-complete")
            except IntegrityError:
                messages.error(request, "Student ID already exists. A member cannot be part of two teams. If not, please contact us!")
        else:
            messages.error(request, "One of the entered data may not be correct or One of the Student IDs already exists. A member cannot be part of two teams. If not, please contact us!")
    else:
        form = ChatGPTForm()
    return render(request, "event_app/chatbot.html", {"form": form})


def robo_race_registration(request):
    if request.method == "POST":
        form = RoboRaceForm(request.POST)
        if form.is_valid():
            RoboRace_instance = form.save()
            student_ids = [RoboRace_instance.team_Lead_StudentID]

            # Handling team lead's student ID
            try:
                RoboRaceMember.objects.create(student_ID=RoboRace_instance.team_Lead_StudentID)
            except IntegrityError:
                messages.error(request, f"Team Lead's Student ID {RoboRace_instance.team_Lead_StudentID} already exists.")

            # Handling member student IDs
            for i in range(2, 5):  # Loop through member fields
                member_id_field = f'member_{i}_StudentID'
                member_id = form.cleaned_data.get(member_id_field)
                if member_id:  # If member ID is not empty
                    try:
                        RoboRaceMember.objects.create(student_ID=member_id)
                    except IntegrityError:
                        messages.error(request, f"Student ID {member_id} already exists.")

            messages.success(request, "Registration successful.")
            return redirect('reg-complete')
        else:
            messages.error(request, "One of the entered data may not be correct or One of the Student IDs already exists. A member cannot be part of two teams. If not, please contact us!")
    else:
        form = RoboRaceForm()
    return render(request, 'event_app/robo_race.html', {'form': form})



def idea_gen_registration(request):
    if request.method == "POST":
        form = IdeaGenForm(request.POST)
        if form.is_valid():
            idea_gen_instance = form.save()  
            student_ids = [idea_gen_instance.team_Lead_StudentID]

            # Handling team lead's student ID
            try:
                IdeaGenMember.objects.create(student_ID=idea_gen_instance.team_Lead_StudentID)
            except IntegrityError:
                messages.error(request, f"Team Lead's Student ID {idea_gen_instance.team_Lead_StudentID} already exists.")

            # Handling member student IDs
            for i in range(2, 5):  # Loop through member fields
                member_id_field = f'member_{i}_StudentID'
                member_id = form.cleaned_data.get(member_id_field)
                if member_id:  # If member ID is not empty
                    try:
                        IdeaGenMember.objects.create(student_ID=member_id)
                    except IntegrityError:
                        messages.error(request, f"Student ID {member_id} already exists.")

            return redirect('reg-complete')  # Update this line
        else:
            messages.error(request, "One of the entered data may not be correct or One of the Student IDs already exists. A member cannot be part of two teams. If not, please contact us!")
    else:
        form = IdeaGenForm()
    return render(request, 'event_app/ideagen.html', {'form': form})
