# Generated by Django 4.1.4 on 2022-12-08 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_match_score_fulltime_awayteam_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='group',
            field=models.CharField(max_length=20, null=True),
        ),
    ]