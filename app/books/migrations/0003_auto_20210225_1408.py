# Generated by Django 3.1.4 on 2021-02-25 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20210224_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbook',
            name='userRate',
            field=models.CharField(choices=[('0', 'None'), ('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')], default='0', max_length=255),
        ),
    ]
