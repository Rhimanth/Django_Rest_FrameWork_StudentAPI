# Generated by Django 5.1.1 on 2025-01-06 12:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('class_id', models.IntegerField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=100)),
                ('class_Mentor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Student_id', models.IntegerField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=200)),
                ('student_gender', models.CharField(max_length=10)),
                ('student_age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_id', models.IntegerField(primary_key=True, serialize=False)),
                ('school_name', models.CharField(max_length=200)),
                ('school_address', models.CharField(max_length=200)),
                ('Standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentApiApp.standard')),
            ],
        ),
        migrations.AddField(
            model_name='standard',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentApiApp.student'),
        ),
    ]
