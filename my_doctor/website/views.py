from django.shortcuts import render

def index(request):
    return render(request,'website/index.html')

def features(request):
    return render(request,'website/how_it_works.html')

def specialty(request):
    return render(request,'website/specialty.html')

def plans(request):
    return render(request,'website/plans.html')

def aboutus(request):
    return render(request,'website/aboutus.html')

def login(request):
    return render(request,'website/login.html')

def contact(request):
    return render(request,'website/contact.html')

def terms_condition(request):
    return render(request,'website/terms_condition.html')

def privacy_policy(request):
    return render(request,'website/privacy_policy.html')

def faq(request):
    return render(request,'website/faq.html')

def doctor_reg(request):
    return render(request,'website/doctor_reg.html')

def forgot_pass(request):
    return render(request,'website/forgot_pass.html')

def PatientRegistration(request):
    return render(request,'website/PatientRegistration.html')