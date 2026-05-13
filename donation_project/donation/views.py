import random
from django.shortcuts import render, redirect
from .models import Donation


def home(request):
    
    if request.method == "POST":

        request.session["name"] = request.POST.get("name")
        request.session["email"] = request.POST.get("email")
        request.session["mobile"] = request.POST.get("mobile")
        request.session["amount"] = request.POST.get("amount")

        return redirect("payment")

    return render(request, "donation/index.html")


def payment(request):

    if request.method == "POST":

        payment_id = f"PAY{random.randint(10000,99999)}"

        donation = Donation.objects.create(
            name=request.session.get("name"),
            email=request.session.get("email"),
            mobile=request.session.get("mobile"),
            amount=request.session.get("amount"),
            payment_id=payment_id,
            payment_status="Success",
        )

        request.session["payment_id"] = payment_id

        return redirect("success")

    context = {
        "name": request.session.get("name"),
        "amount": request.session.get("amount"),
    }

    return render(request, "donation/payment.html", context)


def success(request):

    context = {
        "payment_id": request.session.get("payment_id"),
        "name": request.session.get("name"),
        "amount": request.session.get("amount"),
    }

    return render(request, "donation/success.html", context)
