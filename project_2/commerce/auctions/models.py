from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Auctions(models.Model):
    """Describes an auction.

        It represents:
         # title: name of the offering
         # description: description of the offering
         # date: the date of creation
         # user: the user who owns the offering
         # starting_bid: the amount from where the bidding starts
         # current_bid: the highest bid
    """

    class Meta:
        verbose_name = "auction",
        verbose_name_plural = "auctions"

    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    starting_bid = models.IntegerField()
    current_bid = models.IntegerField()
    picture = models.URLField(null=True)


class Bids(models.Model):
    """Describes all bids.

        It represents:
         # user: the owner of the bid
         # bid: the bid of the user
         # auction: the auction where the bid belongs
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid = models.IntegerField()
    auction = models.ForeignKey(Auctions, on_delete=models.CASCADE)
