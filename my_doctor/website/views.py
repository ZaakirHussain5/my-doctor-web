from django.shortcuts import render
from specialist_type.models import specialist_type
from doctors.models import doctors_info
from django.contrib.auth.models import User

def index(request):

    return render(request,'website/index.html',{
        "page_title":"Welcome to Doctor Plus | India's Most Popular Telemedicine Online Doctor Consultancy.",
        "meta_description":"Doctor Plus | India's most trusted Online Doctor Consultant for General Physician, Dermatology, Psychology, Dietitian, Pediatrician and Gynechology"})

def features(request):
    return render(request,'website/how_it_works.html',{
        "page_title":"How Doctor Consultancy Works.",
        "meta_description":"Consult Online Doctors in just a few clicks, Fast and reliable service with Report Storage, Sample Collection, Lab tests, Medicine Delivery"})

def specialty(request):
    return render(request,'website/specialty.html',{
        "page_title":"Title From Code",
        "meta_description":""})

def plans(request):
    return render(request,'website/plans.html',{
        "page_title":"Doctor Consultancy Plans",
        "meta_description":"Affordable and pocket friendly online doctor consulatation plans with Free follow up, lab discounts, choice of doctor, for your and your family"})

def aboutus(request):
    return render(request,'website/aboutus.html',{
        "page_title":"Doctor Plus | Our Story",
        "meta_description":"Online Telemedicine Video Doctor Consulation program through technology, We plan to reach out to everyone who is connected to the web and offer the best possible health care medical advice possible."})

def login(request):
    return render(request,'website/login.html',{
        "page_title":"Doctor Plus | Login",
        "meta_description":""})

def contact(request):
    return render(request,'website/contact.html',{
        "page_title":"Doctor Plus | Contact Us",
        "meta_description":"Contact us for best in class Online Telemedicine Video Doctor Consulation in General Physician, Dermatology, Psychology, Dietitian, Pediatrician and Gynechology"})

def terms_condition(request):
    return render(request,'website/terms_condition.html',{
        "page_title":"Terms & Conditions",
        "meta_description":"Terms & Conditions"})

def privacy_policy(request):
    return render(request,'website/privacy_policy.html',{
        "page_title":"Privacy Policy",
        "meta_description":"Privacy Policy"})

def faq(request):
    return render(request,'website/faq.html',{
        "page_title":"Frequently Asked Questions",
        "meta_description":"Frequently Asked Questions"})

def doctor_reg(request):
    context = { "specialist_types" : specialist_type.objects.all(),
        "page_title":"Doctor Plus | Doctor Registration",
        "meta_description":"" }
    return render(request,'website/new_doctor_reg.html',context)

def forgot_pass(request):
    return render(request,'website/forgot_pass.html',{
        "page_title":"Reset Password",
        "meta_description":"Password Reset"})

def PatientRegistration(request):
    return render(request,'website/PatientRegistration.html',{
        "page_title":"Doctor Plus | Patient Registration",
        "meta_description":"Registration"})

def doctor_mou_tc(request):
    return render(request,'website/doctors_mou_tc.html',{
        "page_title":"Doctor Plus | MOU Terms and Conditions",
        "meta_description":"MOU Terms and Conditions"})

