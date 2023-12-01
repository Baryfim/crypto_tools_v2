from exchanges import BaseExchange
from utils import RequestBuilder

class OKXExchange(BaseExchange):
    def __init__(self, url: str) -> None:
        super().__init__(url)

    def getAllPurchaseOrders(self: object, coin: str, currency: str, method: str) -> list[dict]:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0',
            'Accept': 'application/json',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://www.okx.com/ru/p2p-markets/usd/buy-usdt',
            'App-Type': 'web',
            'devId': 'ec6c4ae7-c9fe-40f3-bc0e-65683cd1c45e',
            'x-utc': '3',
            'x-zkdex-env': '0',
            'x-cdn': 'https://www.okx.com',
            'x-locale': 'ru_RU',
            'x-site-info': '==QfxojI5RXa05WZiwiIMFkQPx0Rfh1SPJiOiUGZvNmIsICTOJiOi42bpdWZyJye',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJleDExMDE3MDEwODQwMDcxNzcwNUI0RkI4RTM3NERFREFGMW92TmYiLCJ1aWQiOiJHU1ZJbTBpS21QMjZBaStaSEI5M2FRPT0iLCJzdGEiOjAsIm1pZCI6IkdTVkltMGlLbVAyNkFpK1pIQjkzYVE9PSIsImlhdCI6MTcwMTM3MDc1OSwiZXhwIjoxNzAxOTc1NTU5LCJiaWQiOjAsImRvbSI6Ind3dy5va3guY29tIiwiZWlkIjoxLCJpc3MiOiJva2NvaW4iLCJkaWQiOiJvVStHL0ZlVm1qSTQwZFBBdUJTc3N6bDM3RlZCLzhTS2MxamtSaHR0enhlWUdqUlpWMjNoKzdJL1F5SE5YWWZvIiwibGlkIjoiR1NWSW0waUttUDI2QWkrWkhCOTNhUT09Iiwic3ViIjoiNEM3RjU1NUQzNDM0MEQ3ODUyQTlDRUM5MzI1QUMyQTIifQ.UX3pl7g1GNz04lgg8tmONJ-ctseYfRridRBmUc-gawrsPmsqniKaghH_irNbY9sqJxvmZiAXYZiepAFRhn69Yg',
            'Connection': 'keep-alive',
        }

        params = {
            't': '1701370864513',
            'quoteCurrency': currency,
            'baseCurrency': coin,
            'side': 'sell' if method == "BUY" else "buy",
            'paymentMethod': 'all',
            'userType': 'all',
            'showTrade': 'false',
            'showFollow': 'false',
            'showAlreadyTraded': 'false',
            'isAbleFilter': 'false',
            'hideOverseasVerificationAds': 'false',
            'sortType': 'price_asc',
        }
        self.requestBuilder = RequestBuilder(url=self.url, params=params, cookies={}, headers=headers)
        response = self.requestBuilder.getFetch()

        if response and "data" in response:
            return response["data"]['sell' if method.upper() == "BUY" else "buy"]

        return None
