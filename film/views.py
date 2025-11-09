from django.shortcuts import render
from .models import Performance, Movie

def start_view(request):
    mov_list = Movie.objects.all()
    return render(request, 'index.html', {'movies':mov_list})


def about_view(request):
    return render(request, 'about.html ')




def movie_detail_view(request, pk): 
        movie = Movie.objects.filter(id=pk).first()
        per_list = Performance.objects.filter(movie=movie)
        return render(request, 'movie_detail.html ', {'performances':per_list, 'movie':movie})
        
# Create your views here.
