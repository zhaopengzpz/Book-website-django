# Generated by Django 2.1.2 on 2018-11-10 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ireader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chaper',
            name='id',
            field=models.IntegerField(),
        ),
    ]