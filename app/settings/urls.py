from django.contrib import admin
from django.urls import path

from currency.views import banks_list, banks_details, rate_details

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('currency/ratelist/', rate_list),
    path('currency/rate/details/<int:pk>/', rate_details),
    path('currency/bankslist/', banks_list),
    path('currency/bankslist/details1/<int:pk2>/', banks_details),
]
