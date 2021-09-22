from django.db import models


class Rate(models.Model):
    currency_type = models.CharField(max_length=5)
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=50)


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=254)
    subject = models.CharField(max_length=30)
    message = models.CharField(max_length=1024)

    # def save(self, *args, **kwargs):
    #
    #     return super().save(*args, **kwargs)


class Bank(models.Model):  # ht7part1
    name = models.CharField(max_length=30)
    url = models.URLField()
    support = models.EmailField(max_length=254)
