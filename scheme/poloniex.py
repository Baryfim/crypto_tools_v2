from exchanges import PoloniexExchange
from exchanges import BaseExchange


class PoloniexScheme:
    NAME: str = "Poloniex"
    EXCHANGE: BaseExchange = PoloniexExchange
    USER_LINK: str = "$.uid"
    MAX_LIMIT: str = "$.maxTradeLimit"
    MIN_LIMIT: str = "$.minTradeLimit"
    PRICE: str = "$.price"
    EXCHANGE_URL: str = "https://sapi.poloniex.com/spot/otc/advertisement/public/list"
    USER_LINK_TEMPLATE: str = "https://poloniex.com/p2p/merchant/{0}"