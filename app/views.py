from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    qoute = [
        "I am a passionate developer dedicated to facing challenges head-on and has experienced first-hand the transformational power of online learning.",
        "Who likes the challenge of finding and fixing code bugs that may hinder the free flow of code giving the users a more enjoyable and stress-free user experience."
    ]
    return render(request, 'index.html', {'quote': qoute})


# def skills(request):
#     skills = {
#         'skill1' : Skill.objects.filter(skill_type=1),
#         'skill2' : Skill.objects.filter(skill_type=2),
#         'skill3' : Skill.objects.filter(skill_type=3),
#         'skill4' : Skill.objects.filter(skill_type=4),
#     }
#     return render(request, 'skills.html', skills)

# def designs(request):
#     designs = { 'designs' : Design.objects.all() }
#     return render(request, 'design.html', designs)

# def projects(request):
#     projects = { 'projects' : Project.objects.all() }
#     return render(request, 'design.html', projects)