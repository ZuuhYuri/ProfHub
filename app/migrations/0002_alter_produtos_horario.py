# Generated by Django 3.2.7 on 2021-11-25 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='horario',
            field=models.CharField(max_length=10),
        ),
    ]
