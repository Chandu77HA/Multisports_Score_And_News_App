# Generated by Django 4.2.3 on 2023-08-26 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsnews', '0005_alter_saveallindiansportsnews_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saveallindiansportsnews',
            name='author',
            field=models.CharField(blank=True, default='No Author Found', max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='saveallindiansportsnews',
            name='content',
            field=models.TextField(blank=True, default='No Content Found', null=True),
        ),
        migrations.AlterField(
            model_name='saveallindiansportsnews',
            name='published_at',
            field=models.CharField(blank=True, default='No Published Date Found', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='saveallindiansportsnews',
            name='source_name',
            field=models.CharField(blank=True, default='No Title Found', max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='saveallindiansportsnews',
            name='title',
            field=models.CharField(blank=True, default='No Title Found', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='saveallindiansportsnews',
            name='url',
            field=models.URLField(blank=True, default='No URL Found', null=True),
        ),
        migrations.AlterField(
            model_name='saveallindiansportsnews',
            name='url_to_image',
            field=models.URLField(blank=True, default='No Image Link Found', null=True),
        ),
    ]
