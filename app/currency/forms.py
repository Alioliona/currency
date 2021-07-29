from django import forms

from currency.models import Bank, ContactUs


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
