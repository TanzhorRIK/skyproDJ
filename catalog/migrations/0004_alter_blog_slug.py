# Generated by Django 4.2.3 on 2023-08-11 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_blog_alter_product_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]