from exchanges import BaseExchange
from utils import RequestBuilder

class BinanceExchange(BaseExchange):
    def __init__(self, url: str) -> None:
        super().__init__(url)

    def getAllPurchaseOrders(self: object, coin: str, currency: str, method: str) -> list[dict]:
        params = {
            'fiat': currency,
            'page': 1,
            'rows': 10,
            'tradeType': method,
            'asset': coin,
            'countries': [],
            'proMerchantAds': False,
            'shieldMerchantAds': False,
            'publisherType': None,
            'payTypes': [],
            'classifies': ['mass', 'profession'],
        }
        self.requestBuilder = RequestBuilder(url=self.url, params=params, cookies={}, headers={})
        response = self.requestBuilder.postFetch()

        if response and "data" in response:
            return response["data"]

        return None
