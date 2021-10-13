from django.contrib import admin
from purchaseapp.models import (State,City,Party,Product,UOM,Category,PaymentDetails,
PurchaseMaster,PurchaseDetails,GSTwiseSummary,StockTable,Paymentmode)
# Register your models here.

admin.site.register(State)
admin.site.register(City)
admin.site.register(Party)
admin.site.register(Product)
admin.site.register(UOM)
admin.site.register(Category)
admin.site.register(PaymentDetails)
admin.site.register(PurchaseMaster)
admin.site.register(PurchaseDetails)
admin.site.register(GSTwiseSummary)
admin.site.register(StockTable)
admin.site.register(Paymentmode)
