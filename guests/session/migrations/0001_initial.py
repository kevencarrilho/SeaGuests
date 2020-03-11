# Generated by Django 3.0.3 on 2020-03-11 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('nome', models.CharField(max_length=60)),
                ('telefone', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('bairro', models.CharField(max_length=60)),
                ('cidade', models.CharField(max_length=60)),
                ('estado', models.CharField(choices=[('ac', 'AC'), ('al', 'AL'), ('ap', 'AP'), ('am', 'AM'), ('ba', 'BA'), ('ce', 'CE'), ('df', 'DF'), ('es', 'ES'), ('go', 'GO'), ('ma', 'MA'), ('mt', 'MT'), ('ms', 'MS'), ('mg', 'MG'), ('pa', 'PA'), ('pb', 'PB'), ('pr', 'PR'), ('pe', 'PE'), ('pi', 'PI'), ('rj', 'RJ'), ('rn', 'RN'), ('rs', 'RS'), ('ro', 'RO'), ('rr', 'RR'), ('sc', 'SC'), ('sp', 'SP'), ('se', 'SE')], default='pa', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostpot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hostpot', to='manager.Hostpot')),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lead', to='session.Lead')),
            ],
        ),
    ]