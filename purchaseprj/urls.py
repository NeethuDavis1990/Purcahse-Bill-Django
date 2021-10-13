"""purchasebillprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from purchaseapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.initialfunction, name="initialfunction"),
    path('Statecreate_view',views.Statecreate_view,name="Statecreate_view"),
    path('Satelistview',views.Satelistview,name="Satelistview"),
    path('Stateeditview/<int:id>',views.Stateeditview,name="Stateeditview"),
    path('Citycreateview',views.Citycreateview,name="Citycreateview"),
    path('Citylistview',views.Citylistview,name="Citylistview"),
    path('Cityeditview/<int:id>',views.Cityeditview,name="Cityeditview"),
    path('Partyviewcreate',views.Partyviewcreate,name="Partyviewcreate"),
    path('Partylistview',views.Partylistview,name="Partylistview"),
    path('Partyeditview/<int:id>',views.Partyeditview,name="Partyeditview"),
    path('Categorycreateview',views.Categorycreateview,name="Categorycreateview"),
    path('Categorylistview',views.Categorylistview,name="Categorylistview"),
    path('Categoryeditview/<int:id>',views.Categoryeditview,name="Categoryeditview"),
    path('UOMcreateview',views.UOMcreateview,name="UOMcreateview"),
    path('UOMlistview',views.UOMlistview,name="UOMlistview"),
    path('UOMeditview/<int:id>',views.UOMeditview,name="UOMeditview"),
    path('Productcreateview',views.Productcreateview,name="Productcreateview"),
    path('Productlistview',views.Productlistview,name="Productlistview"),
    path('Producteditview/<int:id>',views.Producteditview,name="Producteditview"),
    path('PaymentDetailscreateview',views.PaymentDetailscreateview,name="PaymentDetailscreateview"),
    path('Paymentlistview',views.Paymentlistview,name="Paymentlistview"),
    path('Paymenteditview/<int:id>',views.Paymenteditview,name="Paymenteditview"),
    path('GSTwiseSummarycreateview',views.GSTwiseSummarycreateview,name="GSTwiseSummarycreateview"),
    path('GSTwiseSummarylistview',views.GSTwiseSummarylistview,name="GSTwiseSummarylistview"),
    path('GSTwiseSummaryeditview/<int:id>',views.GSTwiseSummaryeditview,name="GSTwiseSummaryeditview"),
    path('StockTablecreateview',views.StockTablecreateview,name="StockTablecreateview"),
    path('StockTablelistview',views.StockTablelistview,name="StockTablelistview"),
    path('StockTableeditview/<int:id>',views.StockTableeditview,name="StockTableeditview"),
    path('Purchasebillcreateinlineform',views.Purchasebillcreateinlineform,name="Purchasebillcreateinlineform"),
    path('ajax/ValidateStateName/',views.ValidateStateName,name="ValidateStateName"),
    path('ajax/ValidatePartyName/',views.ValidatePartyName,name="ValidatePartyName"),
    path('Paymentmodecreateview',views.Paymentmodecreateview,name="Paymentmodecreateview"),
    path('ajax/CitynamebasedonState/',views.CitynamebasedonState,name="CitynamebasedonState"),
    path('ajax/GetHsnandTax/',views.GetHsnandTax,name="GetHsnandTax"),
    

]
