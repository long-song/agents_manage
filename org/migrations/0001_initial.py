# Generated by Django 2.1.1 on 2019-08-15 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_id', models.IntegerField(primary_key=True, serialize=False)),
                ('menu_name', models.CharField(max_length=30)),
                ('menu_firstmenu', models.IntegerField()),
                ('menu_intro', models.CharField(blank=True, max_length=255, null=True)),
                ('menu_state', models.IntegerField()),
                ('menu_url', models.CharField(blank=True, max_length=255, null=True)),
                ('menu_flag', models.CharField(blank=True, max_length=255, null=True)),
                ('menu_isdel', models.IntegerField()),
            ],
            options={
                'db_table': 'menu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=100)),
                ('role_state', models.IntegerField()),
                ('role_remark', models.CharField(max_length=100)),
                ('role_isdel', models.IntegerField()),
            ],
            options={
                'db_table': 'role',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RoleMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'role_menu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_realname', models.CharField(blank=True, max_length=20, null=True)),
                ('user_logname', models.CharField(blank=True, max_length=20, null=True)),
                ('user_password', models.CharField(blank=True, max_length=20, null=True)),
                ('user_idcard', models.CharField(blank=True, db_column='user_Idcard', max_length=100, null=True)),
                ('user_sex', models.CharField(blank=True, max_length=10, null=True)),
                ('user_address', models.CharField(blank=True, max_length=100, null=True)),
                ('user_email', models.CharField(blank=True, max_length=100, null=True)),
                ('user_starttime', models.DateField(blank=True, null=True)),
                ('user_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('user_state', models.IntegerField(blank=True, null=True)),
                ('user_caiwu', models.IntegerField(blank=True, null=True)),
                ('user_caozuo', models.IntegerField(blank=True, null=True)),
                ('user_isdel', models.IntegerField(blank=True, null=True)),
                ('user_url', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'user_role',
                'managed': False,
            },
        ),
    ]
