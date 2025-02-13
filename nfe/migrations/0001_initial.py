# Generated by Django 3.2 on 2021-04-23 19:09

from django.db import migrations, models
import django.db.models.deletion
import nfe.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('emitentes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nfe',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('serie', models.IntegerField(default=1, verbose_name='Série NFe')),
                ('numero', models.IntegerField(default=1, verbose_name='Número NFe')),
                ('numero_carta_correcao', models.IntegerField(default=0, verbose_name='Número Carta Cor.')),
                ('chave', models.CharField(max_length=44, verbose_name='Chave NFe')),
                ('data_emissao', models.DateField(verbose_name='Emitido Em')),
                ('situacao', models.CharField(max_length=25, verbose_name='Situação')),
                ('status_sefaz', models.CharField(max_length=3, verbose_name='Status Sefaz')),
                ('mensagem_sefaz', models.CharField(max_length=300, verbose_name='Mensagem Sefaz')),
                ('url_xml_nfe', models.FileField(blank=True, null=True, upload_to=nfe.models.nfe_upload_file)),
                ('url_pdf_nfe', models.FileField(blank=True, null=True, upload_to=nfe.models.nfe_upload_file)),
                ('url_xml_cancelado', models.FileField(blank=True, null=True, upload_to=nfe.models.nfe_upload_file)),
                ('url_pdf_cancelado', models.FileField(blank=True, null=True, upload_to=nfe.models.nfe_upload_file)),
                ('url_xml_carta_correcao', models.FileField(blank=True, null=True, upload_to=nfe.models.nfe_upload_file)),
                ('url_pdf_carta_correcao', models.FileField(blank=True, null=True, upload_to=nfe.models.nfe_upload_file)),
                ('emitente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emitentes.emitente')),
            ],
        ),
    ]
