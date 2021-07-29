from django.shortcuts import render, get_object_or_404

from currency.models import Rate, Bank


def banks_list(request):  # ht7part2
    queryset = Bank.objects.all()

    names = []
    for bank in queryset:
        names.append(bank.name)

    context = {
        'names': names,
    }
    return render(request, "bank_list.html", context=context)


def banks_details(request, pk2):  # ht7part3

    # id_ = request.GET['id']
    # bank = Bank.objects.get(pk = pk2)

    bank = get_object_or_404(Bank, pk=pk2)

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
    # id_ = request.GET['id']
    # try:
    #     rate = Rate.objects.get(pk=pk)
    # except Rate.DoesNotExist:
    #     raise Http404(f"Rate does not exist with id {pk}")

    rate = get_object_or_404(Rate, pk=pk)

    context = {
        'object': rate,
    }

    return render(request, 'rate_details.html', context=context)
