# Generated by Django 4.1.1 on 2022-10-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registergame', '0008_alter_game_game_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='game_id',
        ),
        migrations.AddField(
            model_name='game',
            name='sales_id',
            field=models.ManyToManyField(to='registergame.sales'),
        ),
    ]
