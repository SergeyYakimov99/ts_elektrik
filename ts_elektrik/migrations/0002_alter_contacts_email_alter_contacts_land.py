# Generated by Django 4.1.5 on 2023-01-29 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ts_elektrik', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='land',
            field=models.CharField(max_length=50, verbose_name='Страна'),
        ),
    ]