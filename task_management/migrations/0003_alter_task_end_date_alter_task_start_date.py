# Generated by Django 5.0.7 on 2024-08-26 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_management', '0002_rename_due_date_task_end_date_rename_title_task_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
