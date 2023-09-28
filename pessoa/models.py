from django.db import models

class Pessoa(models.Model):
    ESTADO_CIVIL = (
        ('S', 'Solteiro'),
        ('C', 'Casado'),
        ('P', 'Separado'),
        ('D', 'Divorciado'),
        ('V', 'Viuvo')
    )
    nome = models.CharField(max_length=40)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL, blank=False, null=False, default=False)
    
    def __str__(self):
        return self.nome

