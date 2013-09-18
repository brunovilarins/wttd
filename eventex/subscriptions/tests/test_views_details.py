# coding: utf-8

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class DetailTest(TestCase):

    def setUp(self):
        s = Subscription.objects.create(name='Elio Bruno', cpf='12345678910', email='brunovilarins@gmail.com', phone='82-88073078')
        self.resp = self.client.get('/inscricao/%d/' % s.pk)

    def test_get(self):
        'GET /inscricao/1/should return status 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Uses Template'
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    # def test_context(self):
    #     'Context must have a subscription instance.'
    #     subscription = self.resp.context['subscription']
    #     self.assertIsInstance(subscription, Subscription)

