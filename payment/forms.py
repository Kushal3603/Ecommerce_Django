from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    
    shipping_full_name=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}),required=True)
    shipping_email=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),required=True)
    shipping_address=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),required=True)
    shipping_landmark=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Landmark'}),required=False)
    shipping_city=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'City'}),required=True)
    shipping_state=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'State'}),required=True)
    shipping_zipcode=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Zipcode'}),required=True)
    shipping_country=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Country'}),required=True)

    class Meta:
        model=ShippingAddress
        fields=['shipping_full_name','shipping_email','shipping_address','shipping_landmark','shipping_city','shipping_state','shipping_zipcode','shipping_country']
        exclude=['user']

class PaymentForm(forms.Form):
    card_name=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name On Card'}),required=True)
    card_number=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Card Number'}),required=True)
    card_exp_date=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Expiration Date'}),required=True)
    card_cvv_number=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'CVV Code'}),required=True)
    card_address=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Billing Address'}),required=True)
    card_landmark=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Billing Landmark'}),required=False)
    card_city=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Billing City'}),required=True)
    card_state=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Billing State'}),required=True)
    card_zipcode=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Billing Zipcode'}),required=True)
    card_country=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Billing Country'}),required=True)