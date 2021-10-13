
from django.db import models
from django.db.models import deletion
from django.db.models.base import Model
from django.db.models.fields import DecimalField, NullBooleanField
from django.db.models.fields.related import OneToOneField
from django.db.models.lookups import Transform

# Create your models here.

class State(models.Model):
    StateId=models.IntegerField(auto_created=True,primary_key=True)
    StateName=models.CharField(max_length=50,verbose_name="State",null=True,blank=True)
    StateCode=models.IntegerField(verbose_name="State Code",null=True,blank=True,)
    StateAbbr=models.CharField(max_length=5,verbose_name="State Abbr",null=True,blank=True)
    def __str__(self):
        return self.StateName

class City(models.Model):
    CityId=models.IntegerField(auto_created=True,primary_key=True)
    CityName=models.CharField(max_length=50,verbose_name="City",null=True,blank=True)
    State=models.ForeignKey(State,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.CityName

class  Party(models.Model):
    PartyId=models.IntegerField(auto_created=True,primary_key=True)
    PartyName=models.CharField(max_length=100,verbose_name="Supplier")
    GSTNNo=models.CharField(max_length=17,verbose_name="GSTN No",null=True,blank=True)
    State=models.ForeignKey(State,on_delete=models.CASCADE,null=True,blank=True)
    City=models.ForeignKey(City,on_delete=models.PROTECT,null=True,blank=True)
    Shop=models.CharField(max_length=100,verbose_name="Shop Address",null=True,blank=True)
    PartyType=models.CharField(max_length=10,verbose_name="Supplier Type",null=True,blank=True) 
    IsActive=models.IntegerField(verbose_name="Is Active",default=1)
    def __str__(self):
        return self.PartyName

class Category(models.Model):
    Id=models.IntegerField(auto_created=True,primary_key=True)
    CategoryName=models.CharField(max_length=50,verbose_name="Category",null=True,blank=True)
    HSNCode=models.CharField(max_length=10,verbose_name="HSN Code",null=True,blank=True)
    TaxPercentage=models.DecimalField(verbose_name="Tax Percentage",max_digits=10,decimal_places=3,null=True,blank=True)
    def __str__(self):
        return self.CategoryName

class UOM(models.Model):
    Id=models.IntegerField(auto_created=True,primary_key=True)
    Uomtype=models.CharField(max_length=25,verbose_name="UOM")
    UomCode=models.CharField(max_length=10,verbose_name="UOM Code",null=True,blank=True)
    def __str__(self):
        return self.Uomtype

class Product(models.Model):
    ProductId=models.IntegerField(auto_created=True,primary_key=True)
    ProductName=models.CharField(max_length=100,verbose_name="Item",null=True,blank=True)
    ProductCode=models.CharField(max_length=15,verbose_name="Item Code",null=True,blank=True)
    ProductPrice=models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True)
    BaseUOM=models.ForeignKey(UOM,on_delete=models.CASCADE,null=True,blank=True,verbose_name="Base UOM")
    ReorderLevel=models.IntegerField(verbose_name="Reorder Level",null=True,blank=True)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.ProductName

class Paymentmode(models.Model):
    Id=models.IntegerField(auto_created=True,primary_key=True)
    PaymentMode=models.CharField(max_length=25,verbose_name="Payment mode",null=True,blank=True)
    def __str__(self):
        return self.PaymentMode


class PaymentDetails(models.Model):
    Id=models.IntegerField(auto_created=True,primary_key=True)
    PaymentMode=models.ForeignKey(Paymentmode,on_delete=models.CASCADE,verbose_name="Pay Mode",null=True,blank=True)
    PayeeName=models.CharField(max_length=50,verbose_name="Name of Payee",null=True,blank=True)
    CardNo=models.CharField(max_length=25,verbose_name="Card Number",null=True,blank=True)
    ExpDate=models.DateField(verbose_name="Expiry Date",null=True,blank=True)
    Code=models.CharField(max_length=3,verbose_name="Secuirity code",null=True,blank=True)
    def __str__(self):
        return self.PaymentMode

class PurchaseMaster(models.Model):
    Id=models.IntegerField(auto_created=True,primary_key=True)
    InvoiceNo=models.CharField(max_length=25,verbose_name="Invoice No")
    State=models.ForeignKey(State,on_delete=models.CASCADE,verbose_name="Purchase State",null=True,blank=True)
    Supplier=models.ForeignKey(Party,on_delete=models.CASCADE,null=True,blank=True)
    Remarks=models.CharField(max_length=550,null=True,blank=True)
    InvoiceDate=models.DateField(verbose_name="Invoice Date",null=True,blank=True)
    Type=models.CharField(max_length=25,verbose_name="Purchase Type",null=True,blank=True)
    Item=models.ManyToManyField(Product,through="PurchaseDetails",related_name="PurchaseMaster")
    TaxableAmt=models.DecimalField(max_digits=10,decimal_places=3,verbose_name="Taxable Amount",null=True,blank=True)
    CGSTAmnt=models.DecimalField(max_digits=10,decimal_places=3,verbose_name="CGST Amount",null=True,blank=True)
    SGSTAmnt=models.DecimalField(max_digits=10,decimal_places=3,verbose_name="SGST Amount",null=True,blank=True)
    IGSTAmnt=models.DecimalField(max_digits=10,decimal_places=3,verbose_name="IGST Amount",null=True,blank=True)
    Subtotal=models.DecimalField(max_digits=10,decimal_places=3,verbose_name="Purchase Subtotal",null=True,blank=True)
    Discount=models.DecimalField(max_digits=10,decimal_places=3,verbose_name="Purchase Discount",null=True,blank=True)
    GrantTotal=models.DecimalField(max_digits=10,decimal_places=3,verbose_name="Purchase GrantTotal",null=True,blank=True)
    Paymode=models.ForeignKey(Paymentmode,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.InvoiceNo

class PurchaseDetails(models.Model):
    Id=models.IntegerField(auto_created=True,primary_key=True)
    InvoiceNo=models.ForeignKey(PurchaseMaster,on_delete=models.CASCADE,null=True,blank=True)
    Item=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    HSNCode=models.CharField(max_length=20,blank=True,null=True,verbose_name="HSN Code")
    Quantity=models.IntegerField(verbose_name="Qty",null=True,blank=True)
    Rate=models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True)
    UOM=models.ForeignKey(UOM,on_delete=models.PROTECT,null=True,blank=True)
    Disc=models.CharField(max_length=10,blank=True,null=True)
    Taxable=models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True)
    Tax=models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True)
    CGST=models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True)
    SGST=models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True)
    IGST=models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True)
    BaseQty=models.IntegerField(verbose_name="Base Qty",null=True,blank=True)
    Amount=models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True)
    def __str__(self):
        return self.Item

class GSTwiseSummary(models.Model):
    Id=models.IntegerField(auto_created=True,primary_key=True)
    InvoiceNo=models.CharField(max_length=10,verbose_name="Invoice No",null=True,blank=True)
    GSTAmnt=models.DecimalField(max_digits=10,decimal_places=3,verbose_name="GST Amount",null=True,blank=True)
    CGSTAmnt=models.DecimalField(max_digits=10,decimal_places=3,verbose_name="CGST Amount",null=True,blank=True)
    SGTAmnt=models.DecimalField(max_digits=10,decimal_places=3,verbose_name="SGST Amount",null=True,blank=True)
    def __str__(self):
        return self.InvoiceNo

class StockTable(models.Model):
    Id=models.IntegerField(auto_created=True,primary_key=True)
    ProductName=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    StockQty=models.IntegerField(verbose_name="Stock Quantity",null=True,blank=True)
    BaseUOM=models.ForeignKey(UOM,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self):
        return self.ProductName

    
    






