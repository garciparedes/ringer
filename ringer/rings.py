import logging
from abc import ABC, abstractmethod
from typing import Any
from uuid import uuid4

from .exceptions import EmptyRingException

logger = logging.getLogger(__name__)


class Ring(ABC):

    def __init__(self, **kwargs):
        self.uuid = uuid4()

    @abstractmethod
    def append(self, value: Any):
        pass

    @abstractmethod
    def pop(self, index=None) -> Any:
        pass


class RingFile(Ring):
    pass


class RingDirectory(Ring):
    pass


class RingMemory(Ring):

    def __init__(self, size: int, **kwargs):
        super().__init__(**kwargs)
        self._container = dict()
        self._size = size
        self._append_index = 0
        self._pop_index = 0

    @property
    def current_index(self) -> int:
        return self._append_index

    @property
    def size(self) -> int:
        return self._size

    def append(self, value: Any):
        logger.debug('Performing append...')
        logger.debug('append_index: "{}", pop_index: "{}", size: "{}"'.format(
            self._append_index, self._pop_index, self._size))
        self._container[self._append_index] = value
        if self._append_index == self._pop_index:
            self._pop_index = (self._pop_index + 1) % self.size
        self._append_index = (self._append_index + 1) % self._size
        logger.info(self)

    def pop(self, index=None) -> Any:
        if index is not None:
            raise NotImplementedError

        logger.debug('Performing pop...')
        logger.debug('append_index: "{}", pop_index: "{}", size: "{}"'.format(
            self._append_index, self._pop_index, self._size))

        index = self._pop_index

        try:
            value = self._container.pop(index)
        except KeyError as e:
            raise EmptyRingException
        self._pop_index = (self._pop_index + 1) % self.size

        logger.info('{}, {}'.format(self._container, value))
        return value

    def __str__(self):
        return '{}'.format(self._container)
