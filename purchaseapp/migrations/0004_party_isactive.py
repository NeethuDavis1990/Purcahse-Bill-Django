# Generated by Django 3.2.7 on 2021-09-28 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchaseapp', '0003_remove_party_isactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='IsActive',
            field=models.IntegerField(default=1, verbose_name='Is Active'),
        ),
    ]
