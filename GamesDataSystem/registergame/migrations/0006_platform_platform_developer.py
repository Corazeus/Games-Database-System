# Generated by Django 4.1 on 2022-10-17 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registergame', '0005_remove_game_sales_id_sales_game_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='platform',
            name='platform_developer',
            field=models.CharField(default=1, max_length=69),
            preserve_default=False,
        ),
    ]
