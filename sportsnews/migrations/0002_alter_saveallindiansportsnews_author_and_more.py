# Generated by Django 4.2.3 on 2023-08-26 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsnews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saveallindiansportsnews',
            name='author',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='saveallindiansportsnews',
            name='source_name',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='saveallindiansportsnews',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
