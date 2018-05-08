from django.db import models

class Aluno(models.Model):
	ra = models.IntegerField("Numero RA", primary_key=True, null=False)
	nome = models.CharField("Nome", max_length=50)
	email = models.EmailField("Email", max_length=75)
	
	def _str_ (self):
		return self.ra
		
class AtividadeAluno(models.Model):
	ra_aluno = models.IntegerField("RA do Aluno")
	nome_disciplina = models.CharField("Nome da Disciplina", max_length=50)
	semestre_ofertado = models.SlugField("Email", max_length=50)
	ano_ofertado = models.SmallIntegerField("Ano Ofertado")
	sequecial_atividade = models.IntegerField("Sequencial Atividade")
	nota = models.DecimalField ("Nota", max_digits=10, decimal_places=2)
	
	def _str_ (self):
		return self.ra_aluno
		
class Matricula(models.Model):
	ra_aluno = models.IntegerField("RA do Aluno")
	nome_disciplina = models.CharField("Nome da Disciplina", max_length=50)
	ano_ofertado = models.SmallIntegerField("Ano Ofertado")
	semestre_ofertado = models.IntegerField("Semestre Ofertado")
	
	def _str_ (self):
		return self.ra_aluno

class DisciplinaOfertada(models.Model):
	nome_disciplina = models.CharField("Nome da Disciplina",primary_key=True, max_length=50)
	ano = models.SmallIntegerField("Ano", null=False)
	semestre = models.SlugField("Semestre", max_length=50, null=False)
	
	def _str_ (self):
		return self.nome_disciplina

class AtividadeDisciplina(models.Model):
	nome_disciplina = models.CharField("Nome da Disciplina", max_length=50)
	semestre_ofertado = models.IntegerField("Semestre Ofertado")
	ano_ofertado = models.SmallIntegerField("Ano Ofertado")
	sequecial = models.IntegerField("Sequencial")
	data = models.DateField ("Data")
	titulo = models.CharField("Título", max_length=50)
	
	def _str_ (self):
		return self.nome_disciplina
					
class Disciplina(models.Model):
	nome = models.CharField("Nome", max_length=50, primary_key=True, null=False)
	ementa = models.SlugField("Ementa", max_length=350)
	
	def _str_ (self):
		return self.nome	