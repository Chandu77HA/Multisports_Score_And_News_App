# Generated by Django 4.2.3 on 2023-11-01 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricbuzz', '0003_alter_allplayerslist_face_image_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternationalTeams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cricbuzz_team_id', models.PositiveBigIntegerField(unique=True, verbose_name='Cricbuzz Team Id')),
                ('team_name', models.CharField(max_length=500, verbose_name='Team Name')),
                ('team_sub_name', models.CharField(max_length=50, verbose_name='Team Sub Name')),
                ('image_id', models.PositiveBigIntegerField(verbose_name='Cricbuzz Image Id')),
                ('country_name', models.CharField(blank=True, max_length=500, verbose_name='Country Name')),
                ('team_type', models.CharField(choices=[('TEST TEAM', 'Test Team'), ('ASSOCIATE TEAM', 'Associate Team')], max_length=50, verbose_name='Team Type')),
            ],
            options={
                'verbose_name': 'International Team',
                'verbose_name_plural': 'International Teams',
                'ordering': ['cricbuzz_team_id'],
            },
        ),
    ]
