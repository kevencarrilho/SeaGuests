# Generated by Django 3.0.3 on 2020-03-09 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0002_auto_20200309_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='estado',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
