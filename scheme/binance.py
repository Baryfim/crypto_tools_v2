from exchanges import BinanceExchange
from exchanges import BaseExchange


class BinanceScheme:
    NAME: str = "Binance"
    EXCHANGE: BaseExchange = BinanceExchange
    USER_LINK: str = "$.advertiser.userNo"
    MAX_LIMIT: str = "$.adv.dynamicMaxSingleTransAmount"
    MIN_LIMIT: str = "$.adv.minSingleTransQuantity"
    PRICE: str = "$.adv.price"
    EXCHANGE_URL: str = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"
    USER_LINK_TEMPLATE: str = "https://p2p.binance.com/en/advertiserDetail?advertiserNo={0}"