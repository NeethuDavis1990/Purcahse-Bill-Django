from django.forms.models import inlineformset_factory
from django.shortcuts import render,HttpResponse
from purchaseapp.models import (City,State,StockTable,UOM,PurchaseMaster,
PaymentDetails,Product,Party,GSTwiseSummary,Category,PurchaseDetails,Paymentmode)
from purchaseapp.forms import(Cityform,Stateform,StockTableform,UOMform,
PurchaseMasterform,PaymentDetailsform,Productform,Partyform,GSTwiseSummaryform,
Categoryform,PurchaseDetailsform,Paymentmodeform)
from django.http import JsonResponse
# Create your views here.


def initialfunction(request):
    return render(request,'purchaseapp/base.html')

def Statecreate_view(request):
    stateinst=Stateform()
    if request.method=="GET":
        context={'statecreate': stateinst}
        return render(request,'purchaseapp/statecreate.html',context)
    elif request.method=="POST":
        stateobj=Stateform(request.POST)
        if stateobj.is_valid():
            stateobj.save()
            context={'statecreate': stateinst}
            return render(request,'purchaseapp/statecreate.html',context)
        else :
            context={'errror':"error"}
            return render(request,'purchaseapp/statecreate.html',context)


def Satelistview(request):
    if request.method=="GET":
        statelist=State.objects.all()
        context={'statelist':statelist}
        return render(request,'purchaseapp/statelist.html',context)


def Stateeditview(request,id=None):
     stateinst=State.objects.get(StateId=id)
     stateobj=Stateform(instance=stateinst)
     if request.method=="GET":
         context={'statecreate':stateobj}
         return render(request,'purchaseapp/statecreate.html',context)
     elif request.method=="POST":
         stateedit=Stateform(request.POST,instance=stateinst)
         if stateedit.is_valid():
             stateedit.save()
             context={'statecreate':stateedit}
             return render(request,'purchaseapp/statecreate.html',context)

def Citycreateview(request):
    cityinst=Cityform()
    if request.method=="GET":
        context={'citycreate':cityinst}
        return render(request,'purchaseapp/citycreate.html',context)  
    elif request.method=="POST":
        cityobj=Cityform(request.POST)     
        if cityobj.is_valid():
            cityobj.save()
            context={'citycreate':cityinst}
            return render(request,'purchaseapp/citycreate.html',context) 
        else:
            context={'errror':"error"}
            return render(request,'purchaseapp/citycreate.html',context)


def Citylistview(request):
    if request.method=="GET":
        cityinst=City.objects.all()
        context={'citylist':cityinst}
        return render(request,'purchaseapp/citylist.html',context)

def Cityeditview(request,id=None):
     cityinst=City.objects.get(CityId=id)
     cityobj=Cityform(instance=cityinst)
     if request.method=="GET":
        context={'citycreate':cityobj}
        return render(request,'purchaseapp/citycreate.html',context)  
     elif request.method=="POST":
        cityedit=Cityform(request.POST,instance=cityinst)
        if cityedit.is_valid():
            cityedit.save()
            context={'citycreate':cityedit}
            return render(request,'purchaseapp/citycreate.html',context) 

def Partyviewcreate(request):
    partyinst=Partyform()
    if request.method=="GET":
        context={'partycreate':partyinst}
        return render(request,'purchaseapp/partycreate.html',context) 
    elif request.method=="POST":
        partyobj=Partyform(request.POST)
        if partyobj.is_valid():
            partyobj.save()
            context={'partycreate':partyinst}
            return render(request,'purchaseapp/partycreate.html',context) 
        else:
            context={'errror':"error"}
            return render(request,'purchaseapp/partycreate.html',context)


def Partylistview(request):
    if request.method=="GET":
        partylist=Party.objects.all()
        context={'partylist':partylist}
        return render(request,'purchaseapp/partylist.html',context)


def Partyeditview(request,id=None):
     partyinst=Party.objects.get(PartyId=id)
     partyobj=Partyform(instance=partyinst)
     if request.method=="GET":
        context={'citycreate':partyobj}
        return render(request,'purchaseapp/partycreate.html',context)  
     elif request.method=="POST":
        partyedit=Partyform(request.POST,instance=partyinst)
        if partyedit.is_valid():
            partyedit.save()
            context={'citycreate':partyedit}
            return render(request,'purchaseapp/citycreate.html',context) 


def Categorycreateview(request):
    categoryinst=Categoryform()
    if request.method=="GET":
        context={'catcreate': categoryinst}
        return render(request,'purchaseapp/categorycreate.html',context)
    elif request.method=="POST":
        catobj=Categoryform(request.POST)
        if catobj.is_valid():
            catobj.save()
            context={'catcreate': categoryinst}
            return render(request,'purchaseapp/categorycreate.html',context)
        else :
            context={'errror':"error"}
            return render(request,'purchaseapp/categorycreate.html',context)


def Categorylistview(request):
    if request.method=="GET":
        catlist=Category.objects.all()
        context={'catlist':catlist}
        return render(request,'purchaseapp/categorylist.html',context)


def Categoryeditview(request,id=None):
     catinst=Category.objects.get(Id=id)
     catobj=Categoryform(instance=catinst)
     if request.method=="GET":
         context={'catcreate':catobj}
         return render(request,'purchaseapp/categorycreate.html',context)
     elif request.method=="POST":
         catedit=Categoryform(request.POST,instance=catinst)
         if catedit.is_valid():
             catedit.save()
             context={'catcreate':catedit}
             return render(request,'purchaseapp/categorycreate.html',context)


def UOMcreateview(request):
    uominst=UOMform()
    if request.method=="GET":
        context={'uomcreate': uominst}
        return render(request,'purchaseapp/uomcreate.html',context)
    elif request.method=="POST":
        uomobj=UOMform(request.POST)
        if uomobj.is_valid():
            uomobj.save()
            context={'uomcreate': uominst}
            return render(request,'purchaseapp/uomcreate.html',context)
        else :
            context={'errror':"error"}
            return render(request,'purchaseapp/uomcreate.html',context)


def UOMlistview(request):
    if request.method=="GET":
        uomlist=UOM.objects.all()
        context={'uomlist':uomlist}
        return render(request,'purchaseapp/uomlist.html',context)


def UOMeditview(request,id=None):
     uominst=UOM.objects.get(Id=id)
     uomobj=UOMform(instance=uominst)
     if request.method=="GET":
         context={'uomcreate':uomobj}
         return render(request,'purchaseapp/uomcreate.html',context)
     elif request.method=="POST":
         uomedit=UOMform(request.POST,instance=uominst)
         if uomedit.is_valid():
             uomedit.save()
             context={'uomcreate':uomedit}
             return render(request,'purchaseapp/uomcreate.html',context)



def Productcreateview(request):
    productinst=Productform()
    if request.method=="GET":
        context={'productcreate': productinst}
        return render(request,'purchaseapp/productcreate.html',context)
    elif request.method=="POST":
        productobj=Productform(request.POST)
        if productobj.is_valid():
            productobj.save()
            context={'productcreate': productinst}
            return render(request,'purchaseapp/productcreate.html',context)
        else :
            context={'errror':"error"}
            return render(request,'purchaseapp/productcreate.html',context)


def Productlistview(request):
    if request.method=="GET":
        productlist=Product.objects.all()
        context={'productlist':productlist}
        return render(request,'purchaseapp/productlist.html',context)


def Producteditview(request,id=None):
     productinst=Product.objects.get(ProductId=id)
     productobj=Productform(instance=productinst)
     if request.method=="GET":
         context={'productcreate':productobj}
         return render(request,'purchaseapp/productcreate.html',context)
     elif request.method=="POST":
         productedit=Productform(request.POST,instance=productinst)
         if productedit.is_valid():
             productedit.save()
             context={'productcreate':productedit}
             return render(request,'purchaseapp/productcreate.html',context)


            



def PaymentDetailscreateview(request):
    paymentinst=PaymentDetailsform()
    if request.method=="GET":
        context={'paymentcreate': paymentinst}
        return render(request,'purchaseapp/paymentcreate.html',context)
    elif request.method=="POST":
        paymentobj=PaymentDetailsform(request.POST)
        if paymentobj.is_valid():
            paymentobj.save()
            context={'paymentcreate':paymentinst}
            return render(request,'purchaseapp/paymentcreate.html',context)
        else :
            context={'errror':"error"}
            return render(request,'purchaseapp/paymentcreate.html',context)


def Paymentlistview(request):
    if request.method=="GET":
        paymentlist=PaymentDetails.objects.all()
        context={'paymentlist':paymentlist}
        return render(request,'purchaseapp/paymentlist.html',context)


def Paymenteditview(request,id=None):
     paymentinst=PaymentDetails.objects.get(Id=id)
     paymentobj=PaymentDetailsform(instance=paymentinst)
     if request.method=="GET":
         context={'paymentcreate':paymentobj}
         return render(request,'purchaseapp/paymentcreate.html',context)
     elif request.method=="POST":
         paymentedit=PaymentDetailsform(request.POST,instance=paymentinst)
         if paymentedit.is_valid():
             paymentedit.save()
             context={'paymentcreate':paymentedit}
             return render(request,'purchaseapp/paymentcreate.html',context)


            


def GSTwiseSummarycreateview(request):
    gstinst=GSTwiseSummaryform()
    if request.method=="GET":
        context={'gstcreate':gstinst }
        return render(request,'purchaseapp/gstcreate.html',context)
    elif request.method=="POST":
        gstobj=GSTwiseSummaryform(request.POST)
        if gstobj.is_valid():
            gstobj.save()
            context={'gstcreate': gstinst}
            return render(request,'purchaseapp/gstcreate.html',context)
        else :
            context={'errror':"error"}
            return render(request,'purchaseapp/gstcreate.html',context)


def GSTwiseSummarylistview(request):
    if request.method=="GET":
        gstlist=GSTwiseSummary.objects.all()
        context={'gstlist':gstlist}
        return render(request,'purchaseapp/gstlist.html',context)


def GSTwiseSummaryeditview(request,id=None):
     gstinst=GSTwiseSummary.objects.get(Id=id)
     gstobj=GSTwiseSummaryform(instance=gstinst)
     if request.method=="GET":
         context={'gstcreate':gstobj}
         return render(request,'purchaseapp/gstcreate.html',context)
     elif request.method=="POST":
         gstedit=GSTwiseSummaryform(request.POST,instance=gstinst)
         if gstedit.is_valid():
             gstedit.save()
             context={'gstcreate':gstedit}
             return render(request,'purchaseapp/gstcreate.html',context)


            



def StockTablecreateview(request):
    stockinst=StockTableform()
    if request.method=="GET":
        context={'stockcreate':stockinst }
        return render(request,'purchaseapp/stockcreate.html',context)
    elif request.method=="POST":
        stockobj=StockTableform(request.POST)
        if stockobj.is_valid():
            stockobj.save()
            context={'stockcreate': stockinst}
            return render(request,'purchaseapp/stockcreate.html',context)
        else :
            context={'errror':"error"}
            return render(request,'purchaseapp/stockcreate.html',context)


def StockTablelistview(request):
    if request.method=="GET":
        stocklist=StockTable.objects.all()
        context={'stocklist':stocklist}
        return render(request,'purchaseapp/stocklist.html',context)


def StockTableeditview(request,id=None):
     stockinst=StockTable.objects.get(Id=id)
     stockobj=StockTableform(instance=stockinst)
     if request.method=="GET":
         context={'stockcreate':stockobj}
         return render(request,'purchaseapp/stockcreate.html',context)
     elif request.method=="POST":
         stockedit=StockTableform(request.POST,instance=stockinst)
         if stockedit.is_valid():
             stockedit.save()
             context={'stockcreate':stockedit}
             return render(request,'purchaseapp/stockcreate.html',context)


def Paymentmodecreateview(request):
    payinst=Paymentmodeform()
    if request.method=="GET":
        context={'paycreate':payinst }
        return render(request,'purchaseapp/paycreate.html',context)
    elif request.method=="POST":
        payobj=Paymentmodeform(request.POST)
        if payobj.is_valid():
            payobj.save()
            context={'paycreate': payinst}
            return render(request,'purchaseapp/paycreate.html',context)
        else :
            context={'errror':"error"}
            return render(request,'purchaseapp/pay.html',context)
            
def Purchasebillcreateinlineform(request):
     paymentinst=PaymentDetailsform()
     purchaseinst=PurchaseMasterform()
     inlineform=inlineformset_factory(PurchaseMaster,PurchaseDetails,fields=['Item','HSNCode','Quantity','Rate','UOM','Disc','Taxable','Tax','CGST','SGST','IGST','Amount'],extra=1)
     if request.method=="GET":
         inlineinst=inlineform()
         context={'parentform':purchaseinst,'childform':inlineinst,'payment':paymentinst}
         return render(request,'purchaseapp/purchasebillinlinecreate.html',context)
     elif request.method=="POST":
         purchaseobj=PurchaseMasterform(request.POST)
         if purchaseobj.is_valid():
             purchaseobj.save()
             lastpurchaseinst=PurchaseMaster.objects.last()
             itemtoesaved=inlineform(request.POST)
             if itemtoesaved.is_valid():
                 instances=itemtoesaved.save(commit=False)
                 for item in instances:
                     item.InvoiceNo=lastpurchaseinst
                     item.save()
             context={'parentform':purchaseinst,'chilform':purchaseobj,'payment':paymentinst}
             return render(request,'purchaseapp/purchasebillinlinecreate.html',context)

           


def ValidateStateName(request):
    state = request.GET.get('statename', None)
    print(state)
    data = {
        'is_taken': State.objects.filter(StateName__exact=state).exists()
    }
    return JsonResponse(data)

def ValidatePartyName(request):
    party=request.GET.get('partyname',None)
    print(party)
    data={
        'is_taken':Party.objects.filter(PartyName__exact=party).exists()
    }
    return JsonResponse(data)

def CitynamebasedonState(request):
    state=request.GET.get('argstate',None)
    print(state)
    inst=Party.objects.filter()
    return JsonResponse()

def GetHsnandTax(request):
    itemname=request.GET.get('item',None)
    print(itemname)
    itemset=Product.objects.all().values_list('ProductName','Category__CategoryName')
    print(itemset)
    
    hsn=2
    tax=10
    return JsonResponse(hsn,safe=False)