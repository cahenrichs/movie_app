from django.shortcuts import render
from .models import Movie, Director

# Create your views here.
def index(request):
    all_movies = Movie.objects.all
    return render(request, 'index.html', {'all': all_movies})