# Generated by Django 2.1.1 on 2019-08-15 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReportFinaceTb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'report_finace_tb',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReportList',
            fields=[
                ('rep_id', models.AutoField(primary_key=True, serialize=False)),
                ('rep_agentname', models.CharField(blank=True, max_length=20, null=True)),
                ('rep_custerm', models.CharField(blank=True, max_length=20, null=True)),
                ('rep_monty', models.IntegerField(blank=True, null=True)),
                ('rep_nowdate', models.CharField(blank=True, max_length=30, null=True)),
                ('rep_remark', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'report_list',
                'managed': False,
            },
        ),
    ]
