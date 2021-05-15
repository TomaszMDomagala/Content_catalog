# Generated by Django 3.1.6 on 2021-02-10 16:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_auto_20210209_0141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stock',
            options={'ordering': ['-name']},
        ),
        migrations.AlterField(
            model_name='stock',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular stock', primary_key=True, serialize=False),
        ),
    ]
