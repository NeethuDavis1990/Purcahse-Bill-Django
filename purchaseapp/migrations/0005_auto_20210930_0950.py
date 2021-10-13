# Generated by Django 3.2.7 on 2021-09-30 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchaseapp', '0004_party_isactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasedetails',
            name='InvoiceNo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='purchaseapp.purchasemaster'),
        ),
        migrations.AddField(
            model_name='purchasemaster',
            name='Item',
            field=models.ManyToManyField(related_name='PurchaseMaster', through='purchaseapp.PurchaseDetails', to='purchaseapp.Product'),
        ),
        migrations.AlterField(
            model_name='purchasemaster',
            name='Remarks',
            field=models.CharField(max_length=550),
        ),
    ]
