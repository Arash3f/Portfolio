# Generated by Django 3.1.4 on 2021-01-24 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0009_auto_20210121_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='address'),
        ),
        migrations.AddField(
            model_name='user',
            name='call_phone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='call phone'),
        ),
        migrations.AddField(
            model_name='user',
            name='send_email',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='send email'),
        ),
    ]