# Generated by Django 3.1.6 on 2021-02-09 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='name',
            field=models.CharField(default='NULL', help_text='Enter name of the stock', max_length=100),
        ),
    ]
