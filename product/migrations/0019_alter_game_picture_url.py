# Generated by Django 3.2 on 2021-06-02 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='picture_url',
            field=models.ImageField(default='games/default.jpg', upload_to='games'),
        ),
    ]