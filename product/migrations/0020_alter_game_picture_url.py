# Generated by Django 3.2 on 2021-06-02 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_alter_game_picture_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='picture_url',
            field=models.ImageField(blank=True, default='games/default.jpg', null=True, upload_to='games'),
        ),
    ]
