# Generated by Django 4.1.1 on 2022-10-14 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registergame', '0003_alter_game_game_id_alter_game_sales_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='sales',
            field=models.IntegerField(null=True),
        ),
    ]
