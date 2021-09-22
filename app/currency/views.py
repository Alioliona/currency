from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse

from currency.models import Rate, Bank, ContactUs
from currency.forms import BankForm, ContactForm, RateForm
from annoying.functions import get_object_or_None
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


def index(request):
    return render(request, 'index.html')


# def rate_list(request):
#     queryset = Rate.objects.all()
#
#     print(queryset.query)
#     ids = []
#     for rate in queryset:
#         ids.append(rate.id)
#
#     context = {
#             'objects': queryset,
#     }
#
#     return render(request, 'rate_list.html', context=context)

class RateListView(ListView):
    template_name = 'rate_list.html'
    queryset = Rate.objects.all()


# def rate_details(request, pk):
#     rate = get_object_or_404(Rate, pk=pk)
#
#     context = {
#         'object': rate,
#     }
#
#     return render(request, 'rate_details.html', context=context)

class RateDetailView(DetailView):
    template_name='rate_details.html'
    queryset = Rate.objects.all()


# def rate_create(request):
#
#     if request.method == "POST":
#         form_data = request.POST
#         form = RateForm(form_data)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('currency:rate-list'))
#     elif request.method == "GET":
#         form = RateForm()
#
#     context = {
#             'message': 'Rate Create',
#             'form': form,
#             'count': Rate.objects.count(),
#     }
#     return render(request, 'rate_create.html', context=context)

class RateCreateView(CreateView):
    template_name = 'rate_create.html'
    queryset = Rate.objects.all()
    success_url = reverse_lazy('currency:rate-list')
    form_class = RateForm


# def banks_list(request):  # ht7part2
#     queryset = Bank.objects.all()
#
#     context = {
#         'objects': queryset,
#     }
#
#     return render(request, "bank_list.html", context=context)

class BankListView(ListView):
    template_name = 'bank_list.html'
    queryset = Bank.objects.all()

# def banks_details(request, pk):  # ht7part3
#
#     # id_ = request.GET['id']
#     # bank = Bank.objects.get(pk = pk)
#
#     bank = get_object_or_404(Bank, pk=pk)
#
#     context = {
#         'object': bank,
#     }
#     return render(request, "bank_details.html", context=context)


class BankDetailsView(DetailView):
    template_name='bank_details.html'
    queryset = Bank.objects.all()


# def bank_create(request):
#     if request.method == "POST":
#         form_data = request.POST
#         form = BankForm(form_data)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('currency:banks-list'))
#
#     elif request.method == "GET":
#         form = BankForm()
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'bank_create.html', context=context)


class BankCreateView(CreateView):
    template_name = 'rate_create.html'
    queryset = Bank.objects.all()
    success_url = reverse_lazy('currency:banks-list')
    form_class = BankForm


# def bank_update(request, pk):
#     instance = get_object_or_404(Bank, pk=pk)
#
#     if request.method == "POST":
#         form_data = request.POST
#         form = BankForm(form_data, instance=instance)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('currency:banks-list'))
#
#     elif request.method == "GET":
#         form = BankForm(instance=instance)
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'bank_update.html', context=context)


class BankUpdateView(UpdateView):
    template_name = 'bank_update.html'
    queryset = Bank.objects.all()
    success_url = reverse_lazy('currency:banks-list')
    form_class = BankForm


# def bank_delete(request, pk):
#     instance = get_object_or_None(Bank, pk=pk)
#     if instance is not None:
#         instance.delete()
#     return HttpResponseRedirect('/currency/bankslist/')

class RateDeleteView(DeleteView):
    template_name = 'bank_confirm_delete.html'
    queryset = Bank.objects.all()
    success_url = reverse_lazy('currency:banks-list')

# def contactus_create(request):
#
#     if request.method == "POST":
#         form_data = request.POST
#         form = ContactForm(form_data)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/currency/bankslist/')
#     elif request.method == "GET":
#         form = ContactForm()
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'contactus_create.html', context=context)


class CreateContactUs(CreateView):
    model = ContactUs
    fields = (
        'email_from',
        'subject',
        'message',
    )
    success_url = reverse_lazy('index')
    # template = '.html'