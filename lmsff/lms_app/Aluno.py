from django.db import models

class Aluno(models.Model):

    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    celular = models.TextField(max_length=20)
    login = models.TextField(max_length=20)
    senha = models.TextField(max_length=20)

    def save(self):
        if (self.email==''):
            self.email='email nao fornecido'
        super(Aluno,self).save()
