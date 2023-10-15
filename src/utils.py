from abc import ABC, abstractmethod
import json
from base64 import b64encode, b64decode
from typing import Type


class ConvertibleToDict(ABC):
    @abstractmethod
    def to_dict(self) -> dict: ...


class B64Serializable(ConvertibleToDict, ABC):

    def as_base64(self):
        json_bytes = json.dumps(self.to_dict()).encode()
        return b64encode(json_bytes).decode() 

    @staticmethod
    def from_base64(payload: str) -> dict:
        payload = b64decode(payload).decode()
        payload = json.loads(payload)
        return payload
