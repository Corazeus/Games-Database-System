# Generated by Django 4.1.1 on 2022-10-11 14:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registergame', '0002_alter_game_year_released'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='game_img',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]