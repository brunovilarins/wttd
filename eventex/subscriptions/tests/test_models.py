# coding: utf-8

from django.test import TestCase
from eventex.subscriptions.models import Subscription
from datetime import datetime
from django.db import IntegrityError

class SubscriptionTest(TestCase):

    def setUp(self):
        self.obj = Subscription(
            name='Elio Bruno',
            cpf='12345678910',
            email='brunovilarins@gmail.com',
            phone='82-88073078'
        )

    def test_create(self):
        'Subscription must have name, cpf, email, phone.'
        self.obj.save()
        self.assertEqual(1, self.obj.id)

    def test_has_created_at(self):
        'Subscription must have automatic created_at.'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Elio Bruno', unicode(self.obj))


class SubscriptionUniqueTest(TestCase):

    def setUp(self):
        Subscription.objects.create(name='Elio Bruno', cpf='12345678910', email='brunovilarins@gmail.com', phone='82-88073078')

    def test_cpf_unique(self):
        'CPF must be unique.'
        s = Subscription(name='Elio Bruno', cpf='12345678910', email='email@email.com', phone='82-88073078')
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        'Email must be unique.'
        s = Subscription(name='Elio Bruno', cpf='12345678911', email='brunovilarins@gmail.com', phone='82-88073078')
        self.assertRaises(IntegrityError, s.save)


