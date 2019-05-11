from abc import ABC
from typing import Any
from uuid import uuid4

from ..storages import Storage


class Ringer(ABC):

    def __init__(self, storage: Storage, uuid: Any = None, *args, **kwargs):
        if uuid is None:
            uuid = uuid4()
        self.uuid = uuid
        self.storage = storage
