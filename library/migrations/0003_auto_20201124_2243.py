# Generated by Django 3.1.3 on 2020-11-24 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20201124_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=600),
        ),
    ]
