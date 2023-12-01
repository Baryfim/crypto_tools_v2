from exchanges import TreatmentExchange
# Scheme
from scheme import PoloniexScheme
from scheme import BinanceScheme
from scheme import BybitScheme
# Files actions
from utils import FileHandler
import threading, time
import random


class Manager:
    @staticmethod
    def getOrdersByExchange(
        name:                str,
        coin:                str,
        userLink:            str,
        maxLimit:            str,
        minLimit:            str,
        price:               str,
        currency:            str,
        userLink__temapltes: str,
        exchange__obj:       object,
        url_exchange:        str
    ) -> list[dict]:
        responses__result = {}
        exchange__baseExchange = TreatmentExchange(
            name=name,
            coin=coin,
            userLink=userLink,
            maxLimit=maxLimit,
            minLimit=minLimit,
            price=price,
            currency=currency,
            userLink__temapltes=userLink__temapltes
        )
        exchange = exchange__obj(url_exchange)
        # BUY
        __method__ = "BUY"
        exchangeDataBuy = exchange.getAllPurchaseOrders(coin, currency, __method__)
        responses__result[__method__] = (
            exchange__baseExchange.getAll(exchangeDataBuy)
        )


        # SELL
        __method__ = "SELL"
        exchangeDataSell = exchange.getAllPurchaseOrders(coin, currency, __method__)
        responses__result[__method__] = (
            exchange__baseExchange.getAll(exchangeDataSell)
        )
        
        return responses__result

    @staticmethod
    def process_scheme(scheme, coins, currencies, bigdata):
        for coin in coins:
            for currency in currencies:
                if currency not in bigdata.keys():
                     bigdata[currency] = {}
                response__result = Manager.getOrdersByExchange(
                    name=scheme.NAME,
                    coin=coin,
                    userLink=scheme.USER_LINK,
                    maxLimit=scheme.MAX_LIMIT,
                    minLimit=scheme.MIN_LIMIT,
                    price=scheme.PRICE,
                    currency=currency,
                    url_exchange=scheme.EXCHANGE_URL,
                    userLink__temapltes=scheme.USER_LINK_TEMPLATE,
                    exchange__obj=scheme.EXCHANGE
                )
                if "BUY" not in bigdata[currency].keys() and "SELL" not in bigdata[currency].keys():
                    bigdata[currency]["BUY"] = []
                    bigdata[currency]["SELL"] = []

                bigdata[currency]["BUY"] = [*bigdata[currency]["BUY"], *response__result["BUY"]]
                bigdata[currency]["SELL"] = [*bigdata[currency]["SELL"], *response__result["SELL"]]

if __name__ == "__main__":
    schemes = [BinanceScheme, BybitScheme, PoloniexScheme]
    currencies = ["USD"]
    coins = ["USDT"]

    while True:
        bigdata = {}

        threads = []
        for scheme in schemes:
            thread = threading.Thread(target=Manager.process_scheme, args=(scheme, coins, currencies, bigdata))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        hotlinks = []

        for curency in bigdata.keys():
            bigdata[curency]["BUY"] = sorted(bigdata[curency]["BUY"], key=lambda x: list(x.values())[0].get('price'), reverse=False)
            bigdata[curency]["SELL"] = sorted(bigdata[curency]["SELL"], key=lambda x: list(x.values())[0].get('price'), reverse=True)

        # hotlinks = [
        #     bigdata[curency]["BUY"][0],
        #     bigdata[curency]["SELL"][0]
        # ]

        # bigdata[curency]["BUY"].pop(0)
        # bigdata[curency]["SELL"].pop(0)

        fileHandler = FileHandler("data/bigdata.json", "w+")
        fileHandler.recordingReceivedData(bigdata)

        print("[+] Данные были обновлены [+]")
        time.sleep(random.randint(120, 180))

        # minPrice__Buy = list(hotlinks[0].values())[0].get("price")
        # maxPrice__Sell = list(hotlinks[1].values())[0].get("price")

        # procent = f"{str(((maxPrice__Sell - minPrice__Buy) / minPrice__Buy) * 100)[:5]}%"
        # print(procent)