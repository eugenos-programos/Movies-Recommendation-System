from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from .models import Movie
import csv
import os
import re

  
def index(request):
    return render(request, "index.html")

def about(request):
    return HttpResponse("About")

def set(request):   
    # получаем из строки запроса имя пользователя
    username = request.GET.get("username", "Undefined")
    # создаем объект ответа
    response = HttpResponse(f"Hello {username}")
    # передаем его в куки
    response.set_cookie("username", username)
    return response
 
def get(request):
    print(Movie.objects.all())
    return render(request, "index.html")

def upload(request: HttpRequest):
    file_name = request.GET.get("file")
    if not os.path.exists(file_name):
        return HttpResponseNotFound(f"File {file_name} is not found")
    with open(file_name, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        for row in csvreader:
            print(row)
            year = re.findall(r"(\d{4})", row[1])
            year = None if not year else year[-1]
            title = row[1][:row[1].find('(' + year + ')')] if year else row[1]
            print(f"{len(title)} ----- {title}")
            Movie.objects.create(name=title, year=year, genres=row[2])
    return HttpResponse("Dataset uploaded")

def delete(request: HttpResponse):
    Movie.objects.all().delete()
    return render(request, "index.html")
