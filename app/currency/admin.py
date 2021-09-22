from django.contrib import admin
from currency.models import Rate, Bank, ContactUs


class RateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'source',
        'currency_type',
        'buy',
        'sale',
        'created',
    )

    list_filter = (
        'currency_type',
        'source',
        'created',
    )

    search_fields = (
        'currency_type',
        'source',
    )

    readonly_fields = (
        'buy',
        'sale',
    )

    def has_delete_permission(self, request, obj=None):
          return False


admin.site.register(Rate, RateAdmin)


class BankAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'url',
        'support',
    )

    list_filter = (
        'name',
    )

    search_fields = (
        'name',
    )

    # readonly_fields = (
    #     'support',
    # )

    def has_delete_permission(self, request, obj=None):
          return False


admin.site.register(Bank, BankAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'email_from',
        'subject',
        'message',
    )

    list_filter = (
        'email_from',
    )

    search_fields = (
        'message',
    )

    readonly_fields = (
        'email_from',
        'subject',
        'message',
    )

    def has_delete_permission(self, request, obj=None):
          return False

    def has_add_permission(self, request, obj=None):
          return False


admin.site.register(ContactUs, ContactUsAdmin)

