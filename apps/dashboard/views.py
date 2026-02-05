from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View, generic
from django.db.models.functions import TruncDate
from django.db.models import Sum, F 
from apps.items.models import Product, Orders
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
import json


class DashboardView(LoginRequiredMixin,View):
    """
        Dashboard View
    """
    login_url = reverse_lazy('login_view')
    redirect_field_name = 'next'

    def get(self, request):
        top_products = Product.objects.values(
            'product_name'
        ).annotate(total_sales=Sum(F('stock_quantity') * F('cost_per_item'))
        ).order_by('-total_sales')[:10]
        
        
        manufacturer_sales = Product.objects.values(
            'manufacturer__manifacturer_name'
        ).annotate(total_sales=Sum(F('stock_quantity') * F('cost_per_item'))
        ).order_by('-total_sales')
        
        sales = Orders.objects.annotate(
            month=TruncDate('date_ordered')
        ).values('month').annotate(
            sales = Sum(F('quantity') * F('items__cost_per_item'))
        )
        
        Expense = Orders.objects.annotate(
            month=TruncDate('date_ordered')
        ).values('month').annotate(
            expense = Sum(F('quantity') * F('total_amount'))
        )
        
        Profit = Orders.objects.annotate(
            month=TruncDate('date_ordered')
        ).values('month').annotate(
            sales = Sum(F('quantity') * F('items__cost_per_item')),
            expense = Sum(F('quantity') * F('total_amount'))
        ).annotate(
            profit=(F('sales') - F('expense'))
        )
        
        
        return render(request, 'dashboard/home.html', {
            "total_sales": json.dumps(list(top_products)),
            "manufacturer_sales": json.dumps(list(manufacturer_sales)),
            
            "daily_sales": json.dumps(list(sales), cls=DjangoJSONEncoder),
            "daily_expenses": json.dumps(list(Expense), cls=DjangoJSONEncoder),
            "profit": json.dumps(list(Profit), cls=DjangoJSONEncoder)
        })


# create product view
class ProductFormsView(LoginRequiredMixin,generic.CreateView):
    form_class = forms.ProductForm
    template_name = 'dashboard/product_form.html'
    success_url = reverse_lazy('home_view')

class ShipmentFormsView(LoginRequiredMixin,generic.CreateView):
    form_class = forms.ShipmentForm
    template_name = 'dashboard/shipment_form.html'
    success_url = reverse_lazy('home_view')

class OrdersFormsView(LoginRequiredMixin,generic.CreateView):
    form_class = forms.OrdersForm
    template_name = 'dashboard/oder_form.html'
    success_url = reverse_lazy('home_view')

class ManifactureFormsView(LoginRequiredMixin,generic.CreateView):
    form_class = forms.ManufacturerForm
    template_name = 'dashboard/manifacture_form.html'
    success_url = reverse_lazy('home_view')
    