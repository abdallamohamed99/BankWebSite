# Generated by Django 4.2.7 on 2023-12-04 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default='none', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='none', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='salary',
            field=models.CharField(default='none', max_length=255),
        ),
    ]
