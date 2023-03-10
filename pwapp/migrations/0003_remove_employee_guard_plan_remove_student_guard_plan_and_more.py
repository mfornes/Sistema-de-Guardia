# Generated by Django 4.1.5 on 2023-01-11 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pwapp', '0002_guardplan_local'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='guard_plan',
        ),
        migrations.RemoveField(
            model_name='student',
            name='guard_plan',
        ),
        migrations.AddField(
            model_name='guardplan',
            name='employees_first_turn',
            field=models.ManyToManyField(related_name='employee_first_turn', to='pwapp.employee'),
        ),
        migrations.AddField(
            model_name='guardplan',
            name='employees_second_turn',
            field=models.ManyToManyField(related_name='employee_second_turn', to='pwapp.employee'),
        ),
        migrations.AddField(
            model_name='guardplan',
            name='students_first_turn',
            field=models.ManyToManyField(related_name='student_first_turn', to='pwapp.student'),
        ),
        migrations.AddField(
            model_name='guardplan',
            name='students_second_turn',
            field=models.ManyToManyField(related_name='student_second_turn', to='pwapp.student'),
        ),
        migrations.AlterField(
            model_name='guardplan',
            name='local',
            field=models.CharField(choices=[('R', 'Residencia'), ('D', 'Docente')], default='R', max_length=10),
        ),
    ]
