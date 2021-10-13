# Generated by Django 3.2.7 on 2021-10-05 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchaseapp', '0008_alter_purchasemaster_paymode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentdetails',
            name='BankBranch',
        ),
        migrations.RemoveField(
            model_name='paymentdetails',
            name='Chequeno',
        ),
        migrations.RemoveField(
            model_name='paymentdetails',
            name='MobileNo',
        ),
        migrations.AlterField(
            model_name='purchasedetails',
            name='HSNCode',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='HSN Code'),
        ),
        migrations.AlterField(
            model_name='purchasemaster',
            name='Item',
            field=models.ManyToManyField(related_name='PurchaseMaster', through='purchaseapp.PurchaseDetails', to='purchaseapp.Product'),
        ),
    ]
