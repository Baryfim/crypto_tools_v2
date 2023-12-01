from exchanges import BybitExchange
from exchanges import BaseExchange


class BybitScheme:
    NAME: str = "Bybit"
    EXCHANGE: BaseExchange = BybitExchange
    USER_LINK: str = "$.userId"
    MAX_LIMIT: str = "$.maxAmount"
    MIN_LIMIT: str = "$.minAmount"
    PRICE: str = "$.price"
    EXCHANGE_URL: str = "https://api2.bybit.com/fiat/otc/item/online"
    USER_LINK_TEMPLATE: str = "https://www.bybit.com/fiat/trade/otc/profile/{0}/{1}/{2}/item"