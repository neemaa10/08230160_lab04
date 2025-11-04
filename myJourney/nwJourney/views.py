from django.shortcuts import render
from .models import AboutMe, LearningJourney

def index(request):
    entries = LearningJourney.objects.all().order_by('week')
    return render(request, 'index.html', {'entries': entries})

def aboutme(request):
    profile = AboutMe.objects.first()  # Assuming only one profile
    return render(request, 'aboutMe.html', {'profile': profile})
