# Generated by Django 3.2.4 on 2021-07-16 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of Student', max_length=50)),
                ('roll_no', models.IntegerField()),
                ('score', models.IntegerField()),
            ],
        ),
    ]
