from currency.views import (
    RateDetailView, RateCreateView, BankListView, BankDetailsView,
    BankCreateView, BankUpdateView, RateDeleteView,
    CreateContactUs, RateListView
)

from django.urls import path

app_name = 'currency'
urlpatterns = [
    path('ratelist/', RateListView.as_view(), name='rate-list'),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate/details/<int:pk>/', RateDetailView.as_view(), name='rate-details'),
    path('bankslist/', BankListView.as_view(), name='banks-list'),
    path('bankslist/details1/<int:pk>/', BankDetailsView.as_view(), name='banks-details'),
    path('bank-create/', BankCreateView.as_view(), name='bank-create'),
    path('contactus-create/', CreateContactUs.as_view(), name='contact-us'),
    path('bank-update/<int:pk>/', BankUpdateView.as_view(), name='bank-update'),
    path('bank-delete/<int:pk>/', RateDeleteView.as_view(), name='bank-delete'),
]
