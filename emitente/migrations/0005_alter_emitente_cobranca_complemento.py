# Generated by Django 3.2 on 2021-04-12 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emitente', '0004_auto_20210412_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emitente',
            name='cobranca_complemento',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
