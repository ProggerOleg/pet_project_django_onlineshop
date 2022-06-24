# Generated by Django 4.0.4 on 2022-06-19 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0002_alter_category_options_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoplist',
            name='is_published',
        ),
        migrations.AddField(
            model_name='shoplist',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Доступен ли товар'),
        ),
        migrations.AddField(
            model_name='shoplist',
            name='stock',
            field=models.PositiveIntegerField(default=10),
            preserve_default=False,
        ),
    ]
