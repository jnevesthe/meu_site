from django.db import models

class Campo(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=150)
    
    def __str__(self):
        return f'{self.nome} ({self.endereco})'

class Atividade(models.Model):
    numero = models.IntegerField(verbose_name='Número')
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    pontos = models.DecimalField(max_digits=4, decimal_places=1)  # Corrigido: precisa de max_digits e decimal_places
    detalhes = models.CharField(max_length=100)

    campo=models.ForeignKey(Campo, on_delete=models.PROTECT)
    
    def __str__(self):
        return f'{self.numero} ({self.descricao})'
