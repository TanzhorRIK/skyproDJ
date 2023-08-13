# Generated by Django 4.2.3 on 2023-08-13 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_version_alter_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя версии'),
        ),
        migrations.AddField(
            model_name='version',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Версия'),
        ),
        migrations.AddField(
            model_name='version',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.product'),
        ),
        migrations.AddField(
            model_name='version',
            name='status',
            field=models.BooleanField(blank=True, null=True, verbose_name='Статус'),
        ),
    ]
