# Generated by Django 4.1.4 on 2022-12-17 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('area_code', models.CharField(max_length=3, null=True)),
                ('area_flag', models.CharField(max_length=300, null=True)),
                ('area_name', models.CharField(max_length=30, null=True)),
                ('end_date', models.DateField(max_length=10, null=True)),
                ('start_date', models.DateField(max_length=10, null=True)),
                ('emblem', models.CharField(max_length=30, null=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('plan', models.CharField(max_length=30, null=True)),
                ('competition_type', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('utcDateTime', models.DateTimeField()),
                ('utcDate', models.DateField()),
                ('winner', models.CharField(max_length=90, null=True)),
                ('stage', models.CharField(max_length=40, null=True)),
                ('status', models.CharField(max_length=20, null=True)),
                ('awayTeam_score_color', models.CharField(max_length=20, null=True)),
                ('awayTeam_name', models.CharField(max_length=40, null=True)),
                ('awayTeam_shortName', models.CharField(max_length=40, null=True)),
                ('awayTeam_tla', models.CharField(max_length=4, null=True)),
                ('awayTeam_crest_url', models.CharField(max_length=200, null=True)),
                ('homeTeam_score_color', models.CharField(max_length=20, null=True)),
                ('homeTeam_name', models.CharField(max_length=40, null=True)),
                ('homeTeam_shortName', models.CharField(max_length=40, null=True)),
                ('homeTeam_tla', models.CharField(max_length=4, null=True)),
                ('homeTeam_crest_url', models.CharField(max_length=200, null=True)),
                ('comptetition_name', models.CharField(max_length=40, null=True)),
                ('competition_emblem', models.CharField(max_length=400, null=True)),
                ('group', models.CharField(max_length=20, null=True)),
                ('match_duration', models.CharField(max_length=30, null=True)),
                ('score_fullTime_awayTeam', models.IntegerField(null=True)),
                ('score_fullTime_homeTeam', models.IntegerField(null=True)),
            ],
            options={
                'ordering': ('-utcDate',),
            },
        ),
    ]
