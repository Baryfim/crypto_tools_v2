from exchanges import OKXExchange
from exchanges import BaseExchange


class OKXScheme:
    NAME: str = "OKX"
    EXCHANGE: BaseExchange = OKXExchange
    USER_LINK: str = "$.publicUserId"
    MAX_LIMIT: str = "$.quoteMaxAmountPerOrder"
    MIN_LIMIT: str = "$.quoteMinAmountPerOrder"
    PRICE: str = "$.price"
    EXCHANGE_URL: str = "https://www.okx.com/v3/c2c/tradingOrders/books"
    USER_LINK_TEMPLATE: str = "https://www.okx.com/ru/p2p/ads-merchant?publicUserId={0}"