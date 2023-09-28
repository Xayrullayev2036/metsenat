# Generated by Django 4.2.5 on 2023-09-28 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0003_alter_sponsor_options_alter_sponsor_managers_and_more'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='type',
            new_name='student_type',
        ),
        migrations.AlterField(
            model_name='student',
            name='institute',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='student_institute', to='students.institute'),
        ),
        migrations.CreateModel(
            name='StudentSponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('allocated_amount', models.FloatField()),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sponsor', to='sponsor.sponsor')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='student', to='students.student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]