# Generated by Django 3.2.4 on 2021-07-03 17:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_dataset'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
