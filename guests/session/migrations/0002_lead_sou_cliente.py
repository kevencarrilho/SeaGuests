# Generated by Django 3.0.3 on 2020-03-12 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='sou_cliente',
            field=models.BooleanField(default=False),
        ),
    ]