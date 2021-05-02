# Generated by Django 3.1.3 on 2021-05-01 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cohort', '0001_initial'),
        ('Warmups', '0005_auto_20210501_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warmups',
            name='cohort',
        ),
        migrations.AddField(
            model_name='warmups',
            name='cohort',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cohort.cohort'),
            preserve_default=False,
        ),
    ]
