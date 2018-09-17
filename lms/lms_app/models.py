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

class Disciplina(models.Model):
    def __str__(self):
        return self.nome + self.ementa

    def save(self):
        if(len(Disciplina.objects.filter(nome=self.nome))>0):
            raise Exception('disciplina ja utilizada')
        super(Disciplina,self).save()
    
    nome = models.TextField(max_length=50)
    ementa = models.TextField(max_length=5000)

class DisciplinaOfertada(models.Model):
    def __str__(self):
        return self.curso + self.turma + self.ano + self.semestre + self.professor + self.disciplina

    curso = models.TextField(max_length=255)
    turma = models.TextField(max_length=5)
    ano = models.TextField()
    semestre = models.IntegerField()
    professor = models.IntegerField()
    disciplina = models.IntegerField()
    
    def save(self):
        if not(self.curso=='SI' or self.curso=='ADS' or self.curso=='BD'):
            raise Exception('curso INVALIDO')
        super(DisciplinaOfertada,self).save()
