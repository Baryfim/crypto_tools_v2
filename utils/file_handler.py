from utils.file_exception import FileExceptions
import json


class FileHandler:
    def __init__(
        self:   object,
        path:   str,
        method: str
    ) -> None:
        self.path   = path
        self.method = method


    @FileExceptions
    def recordingReceivedData(self, data: list[dict]) -> bool:
        with open(file=self.path, mode="w+") as file_data:
            json.dump(data, file_data, indent=4)
        return True
    

    @FileExceptions
    def readingReceivedData(self) -> list[dict]:
        with open(file=self.path, mode="r+") as file_data:
            return json.load(file_data)
