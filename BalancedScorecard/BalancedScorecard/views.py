from django.http import HttpResponse
from django.shortcuts import render 


def Inicio(request):

    return render(request,"inicio.html")