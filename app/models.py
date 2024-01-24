from django.db import models


class Usuario(models.Model):
    matricula = models.CharField(max_length=14, blank=False, null=False, primary_key=True)
    nome_completo = models.CharField(max_length=250, blank=False, null=False)
    primeiro_nome = models.CharField(max_length=50, blank=False, null=False)
    ultimo_nome = models.CharField(max_length=50, blank=False, null=False)
    cpf = models.CharField(max_length=14, blank=False, null=False, unique=True)
    campus = models.CharField(max_length=4, blank=False, null=False)
    curso = models.CharField(max_length=75, blank=False, null=False)
    email_pessoal = models.EmailField(max_length=250, blank=False, null=False, unique=True)
    email_escolar = models.EmailField(max_length=250, blank=False, null=False, unique=True)
    email_academico = models.EmailField(max_length=250, blank=False, null=False, unique=True)
    sexo = models.CharField(max_length=1, blank=False, null=False)
    tipo_vinculo = models.CharField(max_length=20, blank=False, null=False)
    data_nascimento = models.DateField(blank=False, null=False)
    url_foto = models.URLField(max_length=500, blank=False, null=False)
