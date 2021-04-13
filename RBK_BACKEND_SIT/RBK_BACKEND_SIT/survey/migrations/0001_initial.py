# Generated by Django 3.1.3 on 2021-04-13 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='')),
                ('description', models.TextField(default='')),
                ('url', models.TextField(default='')),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'survey',
            },
        ),
    ]
