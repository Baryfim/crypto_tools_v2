def FileExceptions(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except FileNotFoundError as e:
            print(f"Failed (File Not Found Error): {e}")
            return None
        except FileExistsError as e:
            print(f"Failed (File Exists): {e}")
            return None
        except FileExceptions as e:
            print(f"Failed (File Exceptions): {e}")
            return None

    return wrapper
