# Generated by Django 3.1.4 on 2021-01-20 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0007_auto_20210119_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='github',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='github'),
        ),
        migrations.AlterField(
            model_name='user',
            name='instagram',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='instagram'),
        ),
        migrations.AlterField(
            model_name='user',
            name='telegram',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='telegram'),
        ),
        migrations.AlterField(
            model_name='user',
            name='twitter',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='twitter'),
        ),
    ]
