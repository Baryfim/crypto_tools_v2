from utils import UserLinkFormat
from jsonpath_ng.exceptions import JSONPathError
from jsonpath_ng import parse, Fields
import uuid


class TreatmentExchange:
    def __init__(
        self:                object,
        name:                str,
        coin:                str,
        userLink:            str,
        maxLimit:            str,
        minLimit:            str,
        currency:            str,
        price:               str,
        userLink__temapltes: str
    ) -> None:
        self.name = name
        self.coin = coin
        self.userLink = userLink
        self.maxLimit = maxLimit
        self.minLimit = minLimit
        self.currency = currency
        self.price = price
        self.userLink__temapltes = userLink__temapltes


    def findValue(self, data: dict, metrix: str):
        try:
            jsonpath_expr = parse(metrix)
            match = jsonpath_expr.find(data)

            if match:
                result = match[0].value
                if isinstance(result, Fields):
                    field_name = result.field
                    nested_path = result.path
                    nested_value = self.findPath(data, nested_path)
                    return nested_value[field_name] if nested_value else None
                else:
                    return result
            else:
                return None

        except JSONPathError as ex_jpe:
            print(f"Error finding path: {ex_jpe}")
            return None


    def getItem(self: object, row: dict) -> dict:
        id = str(uuid.uuid4())
        return {
            id: {
                "exchange": self.name,
                "userLink": UserLinkFormat.reformat(
                    self.userLink__temapltes,
                    self.findValue(row, self.userLink),
                    self.coin,
                    self.currency
                ),
                "minLimit": self.findValue(row, self.minLimit),
                "maxLimit": self.findValue(row, self.maxLimit),
                "price": float(self.findValue(row, self.price)),
                "currency": self.currency,
                "coin": self.coin
            }
        }


    def getAll(self, data: list[dict]) -> list[dict]:
        receivedData = []
        for row in data:
            receivedData.append(self.getItem(row))

        return receivedData