# Generated by Django 4.2.3 on 2023-11-01 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricbuzz', '0006_alter_internationalteams_country_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internationalteams',
            name='team_type',
            field=models.CharField(choices=[('Test Team', 'Test Team'), ('Associate Team', 'Associate Team')], max_length=50, verbose_name='Team Type'),
        ),
    ]