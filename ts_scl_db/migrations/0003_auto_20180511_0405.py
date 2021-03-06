# Generated by Django 2.0 on 2018-05-11 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ts_scl_db', '0002_auto_20180510_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene_protein',
            name='GeneName',
            field=models.CharField(default='EMPTY', max_length=150),
        ),
        migrations.AlterField(
            model_name='gene_protein',
            name='GeneSymbol',
            field=models.CharField(default='EMPTY', max_length=150),
        ),
        migrations.AlterField(
            model_name='gene_protein',
            name='UniprotACC',
            field=models.CharField(default='EMPTY', max_length=150),
        ),
        migrations.AlterField(
            model_name='pubannotation',
            name='annotaion',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='pubfulltext',
            name='fulltext',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='pubtokens',
            name='tokens',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='temphighlightedtext',
            name='fulltext',
            field=models.CharField(max_length=10000),
        ),
    ]
