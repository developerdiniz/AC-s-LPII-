from django.db import models

# Create your models here.
class Professor(models.Model):
    def __str__(self):
        return self.nome + self.email + self.celular

    def save(self):
        print('estou salvando!')
        if(self.login == ''):
            raise Exception('login nao enviado')
        if(self.email==''):
            self.email = 'email nao fornecido'
        if(len(Professor.objects.filter(login=self.login))>0):
            raise Exception('login ja utilizado')
        super(Professor,self).save()

    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    celular = models.TextField(max_length=20)
    login = models.TextField(max_length=20)
    senha = models.TextField(max_length=20)