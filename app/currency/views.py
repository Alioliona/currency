from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from currency.models import Rate, Bank
from currency.forms import BankForm, ContactForm
from annoying.functions import get_object_or_None


def banks_list(request):  # ht7part2
    queryset = Bank.objects.all()

    context = {
        'objects': queryset,
    }

    return render(request, "bank_list.html", context=context)


def banks_details(request, pk):  # ht7part3

    # id_ = request.GET['id']
    # bank = Bank.objects.get(pk = pk)

    bank = get_object_or_404(Bank, pk=pk)

    context = {
        'object': bank,
    }
    return render(request, "bank_details.html", context=context)


# def rate_list(request):
#     queryset = Rate.objects.all()
#
#     # print(queryset.query)
#     # ids = []
#     # for rate in queryset:
#     #     ids.append(rate.id)
#
#     context = {
#             'objects' : queryset,
#     }
#
#     return render(request, 'rate_list.html', context=context)

def rate_details(request, pk):
    rate = get_object_or_404(Rate, pk=pk)

    context = {
        'object': rate,
    }

    return render(request, 'rate_details.html', context=context)


def bank_create(request):
    if request.method == "POST":
        form_data = request.POST
        form = BankForm(form_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/bankslist/')

    elif request.method == "GET":
        form = BankForm()

    context = {
        'form': form,
    }

    return render(request, 'bank_create.html', context=context)


def bank_update(request, pk):
    instance = get_object_or_404(Bank, pk=pk)

    if request.method == "POST":
        form_data = request.POST
        form = BankForm(form_data, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/bankslist/')

    elif request.method == "GET":
        form = BankForm(instance=instance)

    context = {
        'form': form,
    }

    return render(request, 'bank_update.html', context=context)


def bank_delete(request, pk):
    instance = get_object_or_None(Bank, pk=pk)
    if instance is not None:
        instance.delete()
    return HttpResponseRedirect('/currency/bankslist/')


def contactus_create(request):

    if request.method == "POST":
        form_data = request.POST
        form = ContactForm(form_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/bankslist/')
    elif request.method == "GET":
        form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'contactus_create.html', context=context)
