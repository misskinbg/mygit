# Generated by Django 2.0.5 on 2019-12-02 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('age', models.IntegerField(default=18, verbose_name='年龄')),
                ('xuehao', models.IntegerField(verbose_name='学号')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
