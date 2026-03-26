from django.db import models

# Create your models here.
class Pessoa(models.Model):
    id = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 100, help_text="Insira o nome")
    idade = models.IntegerField(help_text="Insira a idade")
    email = models.EmailField(max_length = 255, help_text="Informe o email")
    telefone = models.CharField(max_length= 20, help_text="Telefone com DDD e DDI")
    dtNascimento = models.DateField(help_text="Nascimento no formato DD/MM/AAAA", verbose_name="Data de nascimento")

    def __str__(self):
        return self.nome