from django.db import models

class Disciplina(models.Model):
    def __str__(self):
        return self.nome + self.ementa

    def save(self):
        if(len(Disciplina.objects.filter(nome=self.nome))>0):
            raise Exception('disciplina ja utilizada')
        super(Disciplina,self).save()
    
    nome = models.TextField(max_length=50)
    ementa = models.TextField(max_length=5000)