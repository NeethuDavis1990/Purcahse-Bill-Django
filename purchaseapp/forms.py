from purchaseapp.models import (State,City,Party,Category,UOM,
Product,PaymentDetails,PurchaseMaster,Paymentmode,PurchaseDetails,GSTwiseSummary,StockTable)
from django.forms import ModelForm
from django import forms


class Stateform(ModelForm):
    class Meta:
        model=State
        exclude =['StateId']

class Cityform(ModelForm):
    class Meta:
        model=City
        exclude =['CityId']

class Partyform(ModelForm):
    class Meta:
        model=Party
        exclude =['PartyId','IsActive']
       
    

class Categoryform(ModelForm):
    class Meta:
        model=Category
        exclude =['Id']

class UOMform(ModelForm):
    class Meta:
        model=UOM
        exclude =['Id']

class Productform(ModelForm):
    class Meta:
        model=Product
        exclude =['ProductId']

class PaymentDetailsform(ModelForm):
    class Meta:
        model=PaymentDetails
        exclude =['Id']

class PurchaseMasterform(ModelForm):
    class Meta:
        model=PurchaseMaster
        exclude =['Id','Item']

class PurchaseDetailsform(ModelForm):
    class Meta:
        model=PurchaseDetails
        exclude =['Id']


class GSTwiseSummaryform(ModelForm):
    class Meta:
        model=GSTwiseSummary
        exclude =['Id']


class StockTableform(ModelForm):
    class Meta:
        model=StockTable
        exclude =['Id']


class Paymentmodeform(ModelForm):
    class Meta:
        model=Paymentmode
        exclude =['Id']
