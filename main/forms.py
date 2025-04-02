from django import forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PaymentForm(forms.Form):
    full_name = forms.CharField(label="Full Name", max_length=100)
    email = forms.EmailField(label="Email")
    phone = forms.IntegerField(label="Phone Number")
    amount = forms.DecimalField(label="Amount ($)", max_digits=6, decimal_places=2, initial=150.00)
    COURSE_CHOICES = [
        ('crops', 'Fundamentals of Agroecology'),
        ('pests', 'Plant-Based Pest Control'),
        ('soil', 'GIS and Remote Sensing'),
        ('livestock', 'The Future of Livestock'),
    ]

    course = forms.ChoiceField(
        choices=COURSE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Select Course"
    )
    payment_method = forms.ChoiceField(
        choices=[('mpesa', 'M-Pesa'),("paypal", "PayPal")],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Select Payment Method"
    )

# User Signup Form
class FarmerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Require email

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(FarmerSignUpForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = None  # Remove helper texts

class SoilTestForm(forms.Form):
    phone_number = forms.CharField(label="M-Pesa Phone Number", max_length=12)
    latitude = forms.DecimalField(label="Latitude", max_digits=9, decimal_places=6)
    longitude = forms.DecimalField(label="Longitude", max_digits=9, decimal_places=6)
    email = forms.EmailField(label="Your Email")

