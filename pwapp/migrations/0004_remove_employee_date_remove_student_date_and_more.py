# Generated by Django 4.1.5 on 2023-01-18 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pwapp', '0003_remove_employee_guard_plan_remove_student_guard_plan_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='date',
        ),
        migrations.RemoveField(
            model_name='student',
            name='date',
        ),
        migrations.RemoveField(
            model_name='student',
            name='turn',
        ),
    ]
