# Generated by Django 4.2.3 on 2023-09-04 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_todo_duedate_end_todo_duedate_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('Complete', 'Completed'), ('Pending', 'Pending')], max_length=10),
        ),
    ]
