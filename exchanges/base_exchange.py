from utils import RequestBuilder


class BaseExchange:
    def __init__(self, url: str) -> None:
        self.url = url

    def getAllPurchaseOrders(self: object, coin: str, currency: str, method: str) -> list[dict]:
        return None
