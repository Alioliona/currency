from django.contrib import admin
from django.urls import path

from currency.views import (
    rate_details, banks_list, banks_details,
    bank_create, bank_update, bank_delete,
    contactus_create)

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('currency/ratelist/', rate_list),
    path('currency/rate/details/<int:pk>/', rate_details),
    path('currency/bankslist/', banks_list),
    path('currency/bankslist/details1/<int:pk>/', banks_details),
    path('currency/bank-create/', bank_create),
    path('currency/contactus-create/', contactus_create),
    path('currency/bank-update/<int:pk>/', bank_update),
    path('currency/bank-delete/<int:pk>/', bank_delete),
]
