from abc import ABC
from typing import Any
from uuid import uuid4


class Ringer(ABC):

    def __init__(self, uuid: Any = None, **kwargs):
        if uuid is None:
            self.uuid = uuid4()
