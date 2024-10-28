# Generated by Django 4.2.2 on 2024-10-28 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_lesson_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_set', to='study.course', verbose_name='Курс'),
        ),
    ]
