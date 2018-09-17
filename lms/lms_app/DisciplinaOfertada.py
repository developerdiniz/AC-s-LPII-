from django.db import models

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
