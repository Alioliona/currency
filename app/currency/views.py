from django.shortcuts import render

from currency.models import Rate, Bank, ContactUs
from currency.forms import BankForm, RateForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.mail import send_mail


def index(request):
    return render(request, 'index.html')


class RateListView(ListView):
    template_name = 'rate_list.html'
    queryset = Rate.objects.all()


class RateDetailView(DetailView):
    template_name = 'rate_details.html'
    queryset = Rate.objects.all()


class RateCreateView(CreateView):
    template_name = 'rate_create.html'
    queryset = Rate.objects.all()
    success_url = reverse_lazy('currency:rate-list')
    form_class = RateForm


class BankListView(ListView):
    template_name = 'bank_list.html'
    queryset = Bank.objects.all()


class BankDetailsView(DetailView):
    template_name = 'bank_details.html'
    queryset = Bank.objects.all()


class BankCreateView(CreateView):
    template_name = 'rate_create.html'
    queryset = Bank.objects.all()
    success_url = reverse_lazy('currency:banks-list')
    form_class = BankForm


class BankUpdateView(UpdateView):
    template_name = 'bank_update.html'
    queryset = Bank.objects.all()
    success_url = reverse_lazy('currency:banks-list')
    form_class = BankForm


class RateDeleteView(DeleteView):
    template_name = 'bank_confirm_delete.html'
    queryset = Bank.objects.all()
    success_url = reverse_lazy('currency:banks-list')


class CreateContactUs(CreateView):
    model = ContactUs
    fields = (
        'email_from',
        'subject',
        'message',
    )
    # form_class = ContactUsCreate
    success_url = reverse_lazy('index')
    # template = '.html'

    def form_valid(self, form):
        data = form.cleaned_data
        body = f'''
            From: {data['email_from']}
            Topic: {data['subject']}
            Message: {data['message']}
        '''

        send_mail(
            'Contact Us from Client',
            body,
            'testsend.alio@gmail.com',
            ['smash.kudi@gmail.com'],
            fail_silently=False,
        )

        return super().form_valid(form)
