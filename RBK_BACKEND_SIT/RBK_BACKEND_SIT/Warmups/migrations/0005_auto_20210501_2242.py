# Generated by Django 3.1.3 on 2021-05-01 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cohort', '0001_initial'),
        ('Warmups', '0004_warmups_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warmups',
            name='cohort',
        ),
        migrations.AddField(
            model_name='warmups',
            name='cohort',
            field=models.ManyToManyField(to='cohort.Cohort'),
        ),
    ]