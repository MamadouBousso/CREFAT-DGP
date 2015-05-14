# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equation',
            fields=[
                ('id_equation', models.IntegerField(serialize=False, primary_key=True, db_column=b'id_Equation', blank=True)),
                ('type', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'Equation',
            },
        ),
        migrations.CreateModel(
            name='EquationHasOperateur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_equation', models.ForeignKey(db_column=b'id_Equation', blank=True, to='ModelMacro.Equation')),
            ],
            options={
                'db_table': 'Equation_has_Operateur',
            },
        ),
        migrations.CreateModel(
            name='EquationHasParametre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_parametre', models.TextField(db_column=b'nom_Parametre', blank=True)),
                ('id_equation', models.ForeignKey(db_column=b'id_Equation', blank=True, to='ModelMacro.Equation')),
            ],
            options={
                'db_table': 'Equation_has_Parametre',
            },
        ),
        migrations.CreateModel(
            name='EquationHasSequation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_equation', models.ForeignKey(db_column=b'id_Equation', blank=True, to='ModelMacro.Equation')),
            ],
            options={
                'db_table': 'Equation_has_SEquation',
            },
        ),
        migrations.CreateModel(
            name='EquationHasVariable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'Equation_has_Variable',
            },
        ),
        migrations.CreateModel(
            name='Operateur',
            fields=[
                ('nom_operateur', models.TextField(serialize=False, primary_key=True, db_column=b'nom_Operateur', blank=True)),
            ],
            options={
                'db_table': 'Operateur',
            },
        ),
        migrations.CreateModel(
            name='Parametre',
            fields=[
                ('nom_parametre', models.TextField(serialize=False, primary_key=True, db_column=b'nom_Parametre', blank=True)),
                ('valeur', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'Parametre',
            },
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('idprofil', models.IntegerField(serialize=False, primary_key=True, db_column=b'idProfil', blank=True)),
                ('nomprofil', models.TextField(db_column=b'nomProfil', blank=True)),
            ],
            options={
                'db_table': 'Profil',
            },
        ),
        migrations.CreateModel(
            name='Secteur',
            fields=[
                ('id_secteur', models.IntegerField(serialize=False, primary_key=True, db_column=b'id_Secteur', blank=True)),
                ('nom_secteur', models.TextField(db_column=b'nom_Secteur', blank=True)),
            ],
            options={
                'db_table': 'Secteur',
            },
        ),
        migrations.CreateModel(
            name='SEquation',
            fields=[
                ('id_sequation', models.IntegerField(serialize=False, primary_key=True, db_column=b'id_SEquation', blank=True)),
            ],
            options={
                'db_table': 'S_Equation',
            },
        ),
        migrations.CreateModel(
            name='Temps',
            fields=[
                ('annee', models.IntegerField(serialize=False, primary_key=True, blank=True)),
            ],
            options={
                'db_table': 'Temps',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('idusers', models.IntegerField(serialize=False, primary_key=True, db_column=b'idUsers', blank=True)),
                ('prenom', models.TextField(null=True, blank=True)),
                ('nom', models.TextField(null=True, blank=True)),
                ('login', models.TextField(null=True, blank=True)),
                ('password', models.TextField(null=True, blank=True)),
                ('idprofil', models.IntegerField(db_column=b'idProfil', blank=True)),
            ],
            options={
                'db_table': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Valeur',
            fields=[
                ('id_valeur', models.IntegerField(serialize=False, primary_key=True, db_column=b'id_Valeur', blank=True)),
                ('valeur', models.TextField(null=True, blank=True)),
                ('annee', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'Valeur',
            },
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id_variable', models.IntegerField(serialize=False, primary_key=True, db_column=b'id_Variable', blank=True)),
                ('nom_variable', models.TextField(null=True, db_column=b'nom_Variable', blank=True)),
                ('type', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('id_valeur', models.ForeignKey(db_column=b'id_Valeur', blank=True, to='ModelMacro.Valeur', null=True)),
                ('sect_var', models.ForeignKey(db_column=b'sect_var', blank=True, to='ModelMacro.Secteur', null=True)),
            ],
            options={
                'db_table': 'Variable',
            },
        ),
        migrations.AddField(
            model_name='equationhasvariable',
            name='id_Variable',
            field=models.ForeignKey(to='ModelMacro.Variable', db_column=b'id_Variable'),
        ),
        migrations.AddField(
            model_name='equationhasvariable',
            name='id_equation',
            field=models.ForeignKey(to='ModelMacro.Equation', db_column=b'id_Equation'),
        ),
        migrations.AddField(
            model_name='equationhassequation',
            name='id_sequation',
            field=models.ForeignKey(db_column=b'id_SEquation', blank=True, to='ModelMacro.SEquation'),
        ),
        migrations.AddField(
            model_name='equationhasoperateur',
            name='nom_operateur',
            field=models.ForeignKey(db_column=b'nom_Operateur', blank=True, to='ModelMacro.Operateur'),
        ),
    ]
