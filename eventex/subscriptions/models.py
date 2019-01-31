from django.db import models

class Subscription(models.Model):
    name = models.CharField('nome', max_length=180)
    cpf = models.CharField('CPF', max_length=11)
    email = models.EmailField('email')
    phone = models.CharField('telefone', max_length=20)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Inscrições'
        verbose_name = 'Inscrição'

    def __str__(self):
        return self.name