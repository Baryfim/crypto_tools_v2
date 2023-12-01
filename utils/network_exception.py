from requests.exceptions import (
    HTTPError,
    ConnectionError,
    InvalidHeader,
    JSONDecodeError,
    InvalidURL
)

def NetworkExceptions(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except HTTPError as e:
            print(f"Failed (HTTP Error): {e}")
            return None
        except ConnectionError as e:
            print(f"Failed (Connection Error): {e}")
            return None
        except InvalidHeader as e:
            print(f"Failed (Invalid Header): {e}")
            return None
        except JSONDecodeError as e:
            print(f"Failed (Invalid JSON Error): {e}")
            return None
        except InvalidURL as e:
            print(f"Failed (Invalid URL): {e}")
            return None
        except Exception as e:
            print(f"Failed: {e}")
            return None

    return wrapper
