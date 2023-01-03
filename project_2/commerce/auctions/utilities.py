from .models import Auctions, Bids


def create_new_auction_record(record_data: dict) -> Auctions:
    return Auctions(**record_data)


def create_new_bid_record(record_data: dict) -> Bids:
    return Bids(**record_data)

def retrieve_data_for_index_view() -> dict:
    return Auctions.objects.all()

def retrieve_record_count(table: object) -> int:
    return table.objects.all().count()

def bid_is_valid(bid: int, auction_id: int) -> bool:
    current_bid = Auctions.objects.get(pk=auction_id).current_bid
    return bid > current_bid
