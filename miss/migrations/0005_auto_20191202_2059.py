# Generated by Django 2.0.5 on 2019-12-02 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miss', '0004_auto_20191202_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='ee',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True, verbose_name='成绩'),
        ),
    ]
