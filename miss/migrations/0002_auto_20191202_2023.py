# Generated by Django 2.0.5 on 2019-12-02 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miss', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='xuehao',
            field=models.CharField(max_length=11, verbose_name='学号'),
        ),
    ]
