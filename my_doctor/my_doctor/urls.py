from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('frontend.urls')),
    path('',include('website.urls')),
    path('api/',include('accounts.urls')),
    path('api/',include('patients.urls')),
    path('api/',include('doctors.urls')),
    path('api/',include('specialist_type.urls')),
    path('api/',include('consultations.urls')),
    path('api/',include('appointment.urls')),
    path('api/',include('consultant_chat.urls')),
    path('api/',include('subscription_plans.urls')),
    path('api/',include('executive_details.urls')),
    path('doctors/',include('doctorsUI.urls')),
    path('patients/',include('patientsUI.urls')),
    path('api/',include('transactions.urls')),
    path('api/',include('patient_wallet_details.urls')),
    path('api/',include('doctor_payments.urls')),
    path('api/',include('patient_medical_records.urls')),
    path('api/',include('online_enquiry.urls')),
    path('api/',include('reminders.urls')),
    path('social-auth/', include('social_django.urls', namespace="social")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
