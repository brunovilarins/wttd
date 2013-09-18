# coding: utf-8
from django import forms
from django.utils.translation import ugettext as _
from eventex.subscriptions.models import Subscription

class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = Subscription