# Generated by Django 2.0.3 on 2018-05-08 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('ra', models.IntegerField(primary_key=True, serialize=False, verbose_name='Numero RA')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('email', models.EmailField(max_length=75, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='AtividadeAluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ra_aluno', models.IntegerField(verbose_name='RA do Aluno')),
                ('nome_disciplina', models.CharField(max_length=50, verbose_name='Nome da Disciplina')),
                ('semestre_ofertado', models.SlugField(verbose_name='Email')),
                ('ano_ofertado', models.SmallIntegerField(verbose_name='Ano Ofertado')),
                ('sequecial_atividade', models.IntegerField(verbose_name='Sequencial Atividade')),
                ('nota', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Nota')),
            ],
        ),
        migrations.CreateModel(
            name='AtividadeDisciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_disciplina', models.CharField(max_length=50, verbose_name='Nome da Disciplina')),
                ('semestre_ofertado', models.IntegerField(verbose_name='Semestre Ofertado')),
                ('ano_ofertado', models.SmallIntegerField(verbose_name='Ano Ofertado')),
                ('sequecial', models.IntegerField(verbose_name='Sequencial')),
                ('data', models.DateField(verbose_name='Data')),
                ('titulo', models.CharField(max_length=50, verbose_name='Título')),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('nome', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Nome')),
                ('ementa', models.SlugField(max_length=350, verbose_name='Ementa')),
            ],
        ),
        migrations.CreateModel(
            name='DisciplinaOfertada',
            fields=[
                ('nome_disciplina', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Nome da Disciplina')),
                ('ano', models.SmallIntegerField(verbose_name='Ano')),
                ('semestre', models.SlugField(verbose_name='Semestre')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ra_aluno', models.IntegerField(verbose_name='RA do Aluno')),
                ('nome_disciplina', models.CharField(max_length=50, verbose_name='Nome da Disciplina')),
                ('ano_ofertado', models.SmallIntegerField(verbose_name='Ano Ofertado')),
                ('semestre_ofertado', models.IntegerField(verbose_name='Semestre Ofertado')),
            ],
        ),
    ]