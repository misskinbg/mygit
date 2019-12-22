# Generated by Django 2.0.5 on 2019-12-16 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miss', '0007_student_mima'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(default='000001', max_length=6, verbose_name='教师编号')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('zhicheng', models.CharField(max_length=30, verbose_name='职称')),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='date_add',
        ),
    ]