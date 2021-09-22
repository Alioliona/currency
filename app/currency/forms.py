from django import forms

from currency.models import Bank, ContactUs, Rate


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'currency_type',
            'sale',
            'buy',
            'source',
        )


class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = (
            'name',
            'url',
            'support',
        )


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            'email_from',
            'subject',
            'message',
        )
