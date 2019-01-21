from django.core import mail
from django.test import TestCase

class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Patrick', cpf='12345678900',
                    email='patrick.angelis@testmail.com', phone='83 99999-8888')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_mail_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_mail_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_mail_to(self):
        expect = ['contato@eventex.com.br', 'patrick.angelis@testmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_mail_body(self):
        content = (
            'Patrick',
            '12345678900',
            'patrick.angelis@testmail.com',
            '83 99999-8888'
        )
        for text in content:
            with self.subTest():
                self.assertIn(text, self.email.body)
