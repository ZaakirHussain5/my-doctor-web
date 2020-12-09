from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions, generics

from .models import promo_code, AppliedPromoCode
from .serializers import promo_codeSerializer


class promocode_work(viewsets.ModelViewSet):
    serializer_class = promo_codeSerializer
    permissions = [
        permissions.AllowAny
    ]

    queryset = promo_code.objects.all()


class apply_promoCode(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = promo_codeSerializer

    def list(self, request):
        code = request.query_params.get('code')
        total_applied_code = AppliedPromoCode.objects.filter(code__iexact = code, patient=request.user)
        print(total_applied_code)
        
        if total_applied_code.count() == 0:
            promo = promo_code.objects.filter(code__iexact= code)
            if promo.count() >0:
                return Response({
                    'can_applied': True,
                    'code': promo_codeSerializer(promo, many=True).data
                })

            return Response({
                'can_applied': False,
                'message': "Invalid code."
            })


        return Response({
            'can_applied': False,
            'message': "code already used."
        })

        
