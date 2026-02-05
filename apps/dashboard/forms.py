from django import forms
from apps.items.models import Manufacturer, Product, Shipment, Orders


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            css = "w-full px-3 py-2 border rounded"

            # base class
            field.widget.attrs["class"] = css

            # optional per-field logic
            if name in ["description", "notes"]:
                field.widget.attrs["class"] += " h-32"

            # add placeholder automatically
            field.widget.attrs.setdefault(
                "placeholder",
                name.replace("_", " ").title()
            )
    
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            css = "w-full px-3 py-2 border rounded"

            # base class
            field.widget.attrs["class"] = css

            # optional per-field logic
            if name in ["description", "notes"]:
                field.widget.attrs["class"] += " h-32"

            # add placeholder automatically
            field.widget.attrs.setdefault(
                "placeholder",
                name.replace("_", " ").title()
            )

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            css = "w-full px-3 py-2 border rounded"

            # base class
            field.widget.attrs["class"] = css

            # optional per-field logic
            if name in ["description", "notes"]:
                field.widget.attrs["class"] += " h-32"

            # add placeholder automatically
            field.widget.attrs.setdefault(
                "placeholder",
                name.replace("_", " ").title()
            )

class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            css = "w-full px-3 py-2 border rounded"

            # base class
            field.widget.attrs["class"] = css

            # optional per-field logic
            if name in ["description", "notes"]:
                field.widget.attrs["class"] += " h-32"

            # add placeholder automatically
            field.widget.attrs.setdefault(
                "placeholder",
                name.replace("_", " ").title()
            )