# Generated by Django 4.1.4 on 2022-12-08 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_match_awayteam_crest_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='score_fullTime_awayTeam',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='score_fullTime_homeTeam',
            field=models.IntegerField(null=True),
        ),
    ]
