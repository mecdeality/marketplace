# Generated by Django 3.2 on 2021-04-29 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='picture_url',
            field=models.CharField(default='https://pixy.org/src/78/788566.jpg', max_length=255),
        ),
    ]
