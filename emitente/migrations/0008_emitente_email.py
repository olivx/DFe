# Generated by Django 3.2 on 2021-04-13 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emitente', '0007_auto_20210412_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='emitente',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True, verbose_name='E-mail'),
        ),
    ]
