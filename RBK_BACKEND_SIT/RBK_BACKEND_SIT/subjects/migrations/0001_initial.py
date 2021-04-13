# Generated by Django 3.1.3 on 2021-04-13 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('week', '0001_initial'),
        ('days', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='')),
                ('part', models.IntegerField(default=0)),
                ('los', models.TextField(default='')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='days.day')),
                ('week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='week.week')),
            ],
            options={
                'db_table': 'subjects',
            },
        ),
    ]