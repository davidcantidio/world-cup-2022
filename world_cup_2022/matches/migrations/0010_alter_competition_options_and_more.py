# Generated by Django 4.1.4 on 2022-12-21 23:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0009_alter_match_options_remove_match_utcdatetime_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='competition',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='competition',
            name='lastly_accessed',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 21, 23, 17, 3, 301713)),
        ),
    ]
