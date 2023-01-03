from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import utilities
from .models import User
from . import forms
from . import models


def index(request):
    data = utilities.retrieve_data_for_index_view()
    return render(request, "auctions/index.html", {
        "data": data
    })

@login_required(login_url="/login")
def listing(request, id):
    form = forms.BiddingForm(request.POST)
    if request.method == "POST":
        bid = int(request.POST["bid"])
        if (utilities.bid_is_valid(bid, id)):
            auction = models.Auctions.objects.get(pk=id)
            auction.current_bid = bid
            new_bid_record = {
                "user": get_user(request),
                "bid": bid,
                "auction": auction,
            }
            new_bid = models.Bids(**new_bid_record)
            new_bid.save()
            auction.save()

        return HttpResponseRedirect(reverse("index"))
    else:
        data = utilities.retrieve_data_for_index_view().get(pk=id)
        bid_count = utilities.retrieve_record_count(models.Bids)
        return render(request, "auctions/listing.html", {
            "data": data,
            "form": form,
            "bid_count": bid_count
        })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required(login_url="/login")
def create_listing(request):
    form = forms.CreateListingForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            record_data = {
                "title": form.cleaned_data["title"],
                "description": form.cleaned_data["description"],
                "user": get_user(request),
                "starting_bid": form.cleaned_data["starting_bid"],
                "current_bid": form.cleaned_data["starting_bid"],
                "picture": form.cleaned_data["picture"]
            }
            record = utilities.create_new_auction_record(record_data)
            record.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/create_listing.html", {
            "form": form
        })
