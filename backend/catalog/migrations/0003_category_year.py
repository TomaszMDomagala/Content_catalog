# Generated by Django 3.1.6 on 2021-02-10 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20210210_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='year',
            field=models.DateField(blank=True, help_text='Enter year of release', null=True),
        ),
    ]