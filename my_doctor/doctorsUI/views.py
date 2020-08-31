from django.shortcuts import render

def dashboard(request):
    return render(request,'doctorsUI/dashboard.html')