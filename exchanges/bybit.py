from exchanges import BaseExchange
from utils import RequestBuilder

class BybitExchange(BaseExchange):
    def __init__(self, url: str) -> None:
        super().__init__(url)

    def getAllPurchaseOrders(self: object, coin: str, currency: str, method: str) -> list[dict]:
        params = {
            'userId': 32768019,
            'tokenId': coin,
            'currencyId': currency,
            'payment': [],
            'side': '1' if method == "BUY" else '0',
            'size': '10',
            'page': '1',
            'amount': '',
            'authMaker': False,
            'canTrade': False,
        }
        self.requestBuilder = RequestBuilder(url=self.url, params=params, cookies={}, headers={})
        response = self.requestBuilder.postFetch()

        if response and "result" in response:
            return response["result"]["items"]

        return None
