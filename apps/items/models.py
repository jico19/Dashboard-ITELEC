from django.db import models
from shortuuid.django_fields import ShortUUIDField

'''
    Inventory Tables
'''

class  Manufacturer(models.Model):
    manufacturer_id = ShortUUIDField(
        length=16,
        max_length=40,  
        primary_key=True,
        alphabet="ABcDeFg1234",
        prefix="ID_",
        db_index=True,
        editable=False
    )
    
    manifacturer_name = models.CharField(max_length=150, default="")

    
    def __str__(self):
        return self.manifacturer_name.capitalize()

class Product(models.Model):
    
    PRODUCT_TYPE_CHOICES = (
        ('Perishable Goods', 'Perishable Goods'),
        ('Non-Perishable Goods', 'Non-Perishable Goods'),
        ('Consumable Goods', 'Consumable Goods'),
        ('Raw Materials', 'Raw Materials'),
        ('Other', 'Other'),
    )
    
    
    product_id = ShortUUIDField(
        length=16,
        max_length=40,  
        primary_key=True,
        alphabet="ABcDeFg1234",
        prefix="ID_",  
        db_index=True,
        editable=False
    )
    
    product_name = models.CharField(max_length=200, default="")
    product_type = models.CharField(max_length=50,default='Other', choices=PRODUCT_TYPE_CHOICES)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.Model)
    stock_quantity = models.PositiveIntegerField(default=0, null=False)
    cost_per_item = models.PositiveIntegerField(default=0, null=False)

    
    class Meta:
        ordering = ['-stock_quantity']
    
    def __str__(self):
        return f"{self.product_id} - {self.product_name.capitalize()} - {self.product_type} - {self.stock_quantity} - {self.cost_per_item}$"

class Shipment(models.Model):
    
    STATUS_CHOICES = (
        ('On-Transit', 'On-Transit'),
        ('Received', 'Received'),
    )
    
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_shipped = models.DateTimeField(auto_now_add=True)
    shipment_status = models.CharField(max_length=25, default="Received", choices=STATUS_CHOICES)
    
    
    def __str__(self):
        return f"{self.item.product_name} - {self.date_shipped.strftime("%I:%M %p")} - {self.shipment_status}"
    
class Orders(models.Model):
    items = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0, null=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_amount = models.PositiveIntegerField(default=0, null=False)
    
    def __str__(self):
        return f"{self.items.product_name} - {self.quantity} - {self.date_ordered.strftime("%I:%M %p")} - {self.total_amount}"