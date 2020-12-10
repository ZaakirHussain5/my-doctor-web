from django.contrib import admin
from .models import promo_code, AppliedPromoCode

admin.site.register((promo_code, AppliedPromoCode))
