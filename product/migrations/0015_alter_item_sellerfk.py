# Generated by Django 3.2 on 2021-05-15 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('product', '0014_item_sellerfk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sellerFK',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.userstatus'),
        ),
    ]
