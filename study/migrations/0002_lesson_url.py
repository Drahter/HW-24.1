# Generated by Django 4.2.2 on 2024-10-24 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='ссылка'),
        ),
    ]
