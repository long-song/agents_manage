# Generated by Django 2.1.1 on 2019-08-15 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StateTb',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('st_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'state_tb',
                'managed': False,
            },
        ),
    ]
