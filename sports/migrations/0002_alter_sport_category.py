# Generated by Django 4.2.3 on 2023-08-15 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sport',
            name='category',
            field=models.CharField(choices=[('Indoor', 'Indore'), ('Outdoor', 'Outdoor'), ('Dual-Sport', 'Dual-Sport')], max_length=50),
        ),
    ]
