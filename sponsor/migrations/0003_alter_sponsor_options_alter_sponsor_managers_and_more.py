# Generated by Django 4.2.5 on 2023-09-26 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0002_alter_sponsor_payment_amount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sponsor',
            options={'verbose_name': 'Sponsor', 'verbose_name_plural': 'Sponsor'},
        ),
        migrations.AlterModelManagers(
            name='sponsor',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='password',
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='username',
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
