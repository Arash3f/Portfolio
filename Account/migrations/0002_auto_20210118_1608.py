# Generated by Django 3.1.4 on 2021-01-18 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Date',
            field=models.DateField(blank=True, null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='user',
            name='Location',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Location'),
        ),
        migrations.AddField(
            model_name='user',
            name='github',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='github'),
        ),
        migrations.AddField(
            model_name='user',
            name='instagram',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='instagram'),
        ),
        migrations.AddField(
            model_name='user',
            name='job',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='job'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='phone'),
        ),
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='user_pictures/', verbose_name='picture'),
        ),
        migrations.AddField(
            model_name='user',
            name='summery',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='summery'),
        ),
        migrations.AddField(
            model_name='user',
            name='telegram',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='telegram'),
        ),
        migrations.AddField(
            model_name='user',
            name='twitter',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='twitter'),
        ),
    ]