# Generated by Django 3.2 on 2021-04-12 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emitente', '0003_auto_20210412_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emitente',
            name='cobranca_fones',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='emitente',
            name='cpf',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='emitente',
            name='token',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
