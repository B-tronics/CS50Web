from .models import Auctions, Bids


def create_new_auction_record(record_data: dict):
    return Auctions(**record_data)


def create_new_bid_record(record_data: dict):
    return Bids(**record_data)
