# Generated by Django 4.1.1 on 2022-10-14 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registergame', '0009_remove_sales_game_id_game_sales_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='sales_id',
            field=models.ManyToManyField(null=True, to='registergame.sales'),
        ),
    ]
