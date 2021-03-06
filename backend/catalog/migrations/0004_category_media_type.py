# Generated by Django 3.1.6 on 2021-02-10 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_category_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='media_type',
            field=models.CharField(blank=True, choices=[('m', 'music'), ('f', 'films'), ('s', 'series'), ('b', 'books'), ('g', 'games'), ('o', 'other')], default='0', help_text='Type of your media', max_length=1),
        ),
    ]
