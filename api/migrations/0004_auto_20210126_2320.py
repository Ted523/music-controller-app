# Generated by Django 3.0.7 on 2021-01-26 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210126_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='guest_can_pause',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
