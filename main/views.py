import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django_daraja.mpesa.core import MpesaClient

from main.forms import PaymentForm, SoilTestForm
from main.models import Course, Article
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import FarmerSignUpForm


# Create your views here.
@login_required
def home(request):
    crops = Article.objects.filter(category='Crops')
    livestock = Article.objects.filter(category='Livestock')
    soil = Article.objects.filter(category='Soil')
    pests = Article.objects.filter(category='Pests')
    smart_agri = Article.objects.filter(category='SmartAgri')

    context = {
        'crops': crops,
        'livestock': livestock,
        'soil': soil,
        'pests': pests,
        'smart_agri': smart_agri,
    }

    return render(request, 'home.html', context)


@login_required
def courseone(request):

    return render(request, 'courseone.html')


def payment_page(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Process Payment (Dummy Step)
            messages.success(request, "Payment successful! Thank you for enrolling.")
            return redirect("courseone")
    else:
        form = PaymentForm()

    return render(request, "payment_form.html", {"form": form})


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    # If the course has a custom HTML template, render it
    if course.courseone:
        return render(request, f'courses/{course.courseone}.html', {'course': course})

    # Otherwise, use a default course template
    return render(request, 'courseone.html', {'course': course})


def search_results(request):
    query = request.GET.get('q', '')  # Get the search term
    results = Course.objects.filter(title__icontains=query) if query else []  # Search by title

    return render(request, 'result_page.html', {'query': query, 'results': results})


# Signup View
def signup(request):
    if request.method == "POST":
        form = FarmerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after signup
            return redirect('home')  # Redirect to a dashboard or homepage
    else:
        form = FarmerSignUpForm()

    return render(request, 'signup.html', {'form': form})


# Login View
def farmerlogin(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect after login
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


# Logout View
def farmerlogout(request):
    logout(request)
    return redirect('login')


def contact(request):
    return render(request, 'contact.html')


def trigger(request):
    cl = MpesaClient()
    phone_number = '0115222742'
    amount = 1
    account_reference = '001-ABC'
    transaction_desc = 'Soil Testing Services'
    callback_url = 'https://7c57-2c0f-fe38-232c-d406-b1b7-2315-d088-196.ngrok-free.app/callback'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)


@csrf_exempt
def callback(request):
    result = json.loads(request.body)
    print(result)
    return HttpResponse("OK")


MPESA_AMOUNT = 1





def services_payment(request):
    if request.method == "POST":
        form = SoilTestForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data["phone_number"]
            latitude = form.cleaned_data["latitude"]
            longitude = form.cleaned_data["longitude"]
            email = form.cleaned_data["email"]

            # Initialize M-Pesa client
            cl = MpesaClient()
            account_reference = "SoilTest"
            transaction_desc = "Payment for Soil Testing"
            callback_url = "https://your-ngrok-url.ngrok-free.app/callback"  # Replace with actual callback URL

            # Trigger M-Pesa STK Push
            response = cl.stk_push(phone_number, MPESA_AMOUNT, account_reference, transaction_desc, callback_url)

            # Ensure response is valid before proceeding
            if response.response_code == "0":
                messages.success(request, "Payment request sent to your phone. Please complete payment.")
                return redirect("payment_success")  # Redirect to success page
            else:
                messages.error(request, "Payment failed. Please try again.")
                return render(request, "services_payment.html", {"form": form})  # ✅ Return response even if STK fails

    else:
        form = SoilTestForm()  # ✅ Only initialize a new form in GET requests

    return render(request, "services_payment.html", {"form": form})  # ✅ Always return a response



def payment_success(request):
    return render(request, "payment_success.html")

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article': article})