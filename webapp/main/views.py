from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'main/index.html')

def resume(request):
    return render(request, 'main/resume.html')

def findTeam(request):
    data = {
        'profile': {'name': 'Ivan', 'city': 'Moskow', 'exp': "Мой первый хакатон", 'edu': "МГУ",
                    'mail': "rabochiya00@mail.ru", 'p_num': "+7(999)888-77-43", 'about': "Опыт работы 5 лет. Бэк-разработчик, язык Python, Java. "}
    }
    return render(request, 'main/contactinfo2.html', data)

def findMember(request):
    return render(request, 'main/memberfinder.html')


def noProfile(request):
    return render(request, 'main/noProfile.html')