from exchanges import BaseExchange
from utils import RequestBuilder

class PoloniexExchange(BaseExchange):
    def __init__(self, url: str) -> None:
        super().__init__(url)

        self.coins = ["USDT", "BTC"]
        self.currencys = ['USD', 'SGD', 'INR', 'VND', 'CAD', 'AUD', 'TWD', 'RUB', 'GBP', 'HKD', 'EUR', 'NGN', 'IDR', 'PHP', 'KHR', 'BRL', 'AED', 'MYR', 'TRY', 'THB', 'UAH', 'GEL', 'KZT', 'PKR', 'MOP']

    def getAllPurchaseOrders(self: object, coin: str, currency: str, method: str) -> list[dict]:
        if coin not in self.coins:
            return None
        
        params = {
            'quoteAssetId': self.currencys.index(currency) + 2,
            'coinId': '1' if coin == "BTC" else '2',
            'tradeType': '2' if method == "BUY" else '1',
            'page': '1',
        }
        self.requestBuilder = RequestBuilder(url=self.url, params=params, cookies={}, headers={})
        response = self.requestBuilder.getFetch()

        if response and "data" in response:
            return response["data"]["list"]

        return None







