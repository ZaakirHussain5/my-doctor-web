from rest_framework import viewsets, permissions,generics,status
from rest_framework.response import Response
from datetime import date, timedelta
from .serializers import PatientSubscriptionSerializers
from .models import PatientSubscription
from subscription_plans.models import subscription_plans
from patients.models import patient_info,PatientBillingHistory
from django.http import JsonResponse
from rest_framework.response import Response

plans = [
  {
    "id":"1",
    "plan": "Individual",
    "coverge": "One",
    "Validity": "10 Consults",
    "FreeVideo/AudioConsult": "YES",
    "UnlimitedConsult/month": "NO",
    "LabDiscounts": "YES",
    "FreeFollowups": "2",
    "ReportStorage": "YES",
    "SpecialityChoise": "YES",
    "ChoiceofDoctor": "YES",
    "Price": "2490",
    "description":"Plan Description"
  },
  {
    "id":"2",
    "plan": "You + 1",
    "coverge": "You + 1 Child",
    "Validity": "15 Consults",
    "FreeVideo/AudioConsult": "YES",
    "UnlimitedConsult/month": "NO",
    "LabDiscounts": "YES",
    "FreeFollowups": "2",
    "ReportStorage": "YES",
    "SpecialityChoise": "YES",
    "ChoiceofDoctor": "YES",
    "Price": "2990",
    "description":"Plan Description"
  },
  {
    "id":"3",
    "plan": "You + 2",
    "coverge": "You + 1 Adult + 1 Child",
    "Validity": "15 Consults",
    "FreeVideo/AudioConsult": "YES",
    "UnlimitedConsult/month": "NO",
    "LabDiscounts": "YES",
    "FreeFollowups": "2",
    "ReportStorage": "YES",
    "SpecialityChoise": "YES",
    "ChoiceofDoctor": "YES",
    "Price": "4990",
    "description":"Plan Description"
  },
  {
    "id":"4",
    "plan": "You + 3",
    "coverge": "You + 1 Adult + 2 Child",
    "Validity": "15 Consults",
    "FreeVideo/AudioConsult": "YES",
    "UnlimitedConsult/month": "NO",
    "LabDiscounts": "YES",
    "FreeFollowups": "2",
    "ReportStorage": "YES",
    "SpecialityChoise": "YES",
    "ChoiceofDoctor": "YES",
    "Price": "5990",
    "description":"Plan Description"
  },
  {
    "id":"5",
    "plan": "Senior Citizens",
    "coverge": "One",
    "Validity": "One Month",
    "FreeVideo/AudioConsult": "YES",
    "UnlimitedConsult/month": "YES",
    "LabDiscounts": "YES",
    "FreeFollowups": "4",
    "ReportStorage": "YES",
    "SpecialityChoise": "YES",
    "ChoiceofDoctor": "YES",
    "Price": "4990",
    "description":"Plan Description"
  }
]

def getPlans(request):
    return JsonResponse(plans,safe=False)

class subscribeToAPlan(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def post(self, request, *args, **kwargs):
        data = request.data
        if "planId" not in data.keys():
            return Response({"error":"planId is Required"},status=status.HTTP_400_BAD_REQUEST)
        if "payment_id" not in data.keys():
            return Response({"error":"payment_id is Required"},status=status.HTTP_400_BAD_REQUEST)
        if data["planId"] == "":
            return Response({"error":"planId can't be blank"},status=status.HTTP_400_BAD_REQUEST)
        plan = {}
        for p in plans:
            if data["planId"] == p["id"]:
                plan = p
                break
        if plan == {}:
            return Response({"error":"Invalid planId"},status=status.HTTP_400_BAD_REQUEST)

        consCount = plan["Validity"].split(' ')[0]
        is_senior = False
        user = patient_info.objects.get(user=request.user)
        if p["id"] == "5":
            if user.age == None or user.age == '':
                return Response({"error":"Update Your Age for elegiblity"},status=status.HTTP_400_BAD_REQUEST)
            else:
                if int(user.get_age) >= 65:
                    is_senior = True
                else:
                    return Response({"error":"Not Elegible for Senior Citizen Plan"},status=status.HTTP_400_BAD_REQUEST)

        
        PatientSubscription.objects.filter(user=user).delete()
        subscription = PatientSubscription.objects.create(payment_id=data["payment_id"],
        cons_count=consCount,total_count=consCount,
        is_active=True,is_senior=is_senior,
        plan_description=plan["description"],paid_amount=plan["Price"],
        plan_price=plan["Price"],gst=18.00,plan=plan["plan"],user=user)

        PatientBillingHistory.objects.create(patient=user,doc_name=plan['plan'] + " Plan",
        doc_spl="Subscrition Plan Activated",amount=plan['Price'],
        description="Amount Deducted for Subscription",
        doc_image='2.png',status="P")

        return Response({
            "Message":"Plan Subscriped Successfully",
            "plan":PatientSubscriptionSerializers(subscription, context=self.get_serializer_context()).data
        })


class MySubscriptionPlans(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PatientSubscriptionSerializers

    def get_queryset(self):
        user = patient_info.objects.get(user=self.request.user)
        return PatientSubscription.objects.filter(user=user, is_active=True)

    def perform_create(self, serializer):
        user = patient_info.objects.get(user=self.request.user)
        PatientBillingHistory.objects.create(patient=user,doc_name=self.request.data['plan'] + " Plan",
        doc_spl="Subscrition Plan Activated",amount=self.request.data['paid_amount'],
        description="Amount Deducted for Subscription",
        doc_image='2.png',status="P")
        return serializer.save(user = user,total_count=self.request.data['cons_count'])
        

class allSubscriptionForAdmin(viewsets.ModelViewSet):
    serializer_class = PatientSubscriptionSerializers
    permissions = [
        permissions.AllowAny
    ]

    queryset = PatientSubscription.objects.all()