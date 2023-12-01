from utils.network_exception import NetworkExceptions
import requests as rq


class RequestBuilder:
    def __init__(
        self:    object,
        url:     str,
        params:  dict,
        cookies: dict,
        headers: dict
    ) -> None:
        self.url     = url
        self.params  = params
        self.cookies = cookies
        self.headers = headers


    @NetworkExceptions
    def getFetch(self):
        response = rq.get(
            url=self.url,
            params=self.params,
            cookies=self.cookies,
            headers=self.headers
        )
        return response.json()


    @NetworkExceptions
    def postFetch(self):
        response = rq.post(
            url=self.url,
            json=self.params,
            cookies=self.cookies,
            headers=self.headers
        )
        return response.json()
