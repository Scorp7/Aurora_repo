# Generated by Django 3.2 on 2021-04-23 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturant', '0003_auto_20210422_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(blank=True, choices=[(True, 'Reserved'), (False, 'Unreserved'), ('1', 'Undefined')], default='1', max_length=10),
        ),
    ]
