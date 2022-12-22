# Generated by Django 4.1.4 on 2022-12-19 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0003_match_competition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='competition_emblem',
        ),
        migrations.RemoveField(
            model_name='match',
            name='comptetition_name',
        ),
        migrations.AlterField(
            model_name='match',
            name='competition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matches.competition'),
        ),
    ]