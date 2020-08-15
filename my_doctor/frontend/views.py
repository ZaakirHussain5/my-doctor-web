from django.shortcuts import render

def login(request):
    return render(request,'auth/login.html')

def dashboard(request):
    return render(request,'auth/dashboard.html')

def specialists(request):
    return render(request,'frontend/specialists.html')

def newDoctor(request):
    return render(request,'frontend/newDoctor.html')

def doctorsList(request):
    return render(request,'frontend/doctorsList.html')

def newExecutive(request):
    return render(request,'frontend/newExecutive.html')

def executivesList(request):
    return render(request,'frontend/executivesList.html')