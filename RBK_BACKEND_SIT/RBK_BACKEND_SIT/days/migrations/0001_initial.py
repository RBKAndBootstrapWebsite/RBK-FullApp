# Generated by Django 3.1.3 on 2021-04-13 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('week', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
                ('week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='week.week')),
            ],
            options={
                'db_table': 'days',
            },
        ),
    ]
