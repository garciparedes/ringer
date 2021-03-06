import logging

from typing import Any

from ..storages import Storage
from ..exceptions import EmptyRingerException
from .base import Ringer

logger = logging.getLogger(__name__)


class RingerDeque(Ringer):

    def __init__(self, capacity: int, **kwargs):

        if kwargs.get('storage') != Storage.MEMORY:
            raise NotImplementedError

        super().__init__(**kwargs)
        self._container = dict()
        self._capacity = capacity
        self._append_index = 0
        self._pop_index = 0

    @property
    def current_index(self) -> int:
        return self._append_index

    @property
    def capacity(self) -> int:
        return self._capacity

    def __len__(self) -> int:
        return len(self._container)

    def append(self, value: Any):
        logger.debug('Performing append()...')
        logger.debug('append_index: "{}", pop_index: "{}", size: "{}"'.format(
            self._append_index, self._pop_index, self._capacity))
        self._container[self._append_index] = value
        if self._append_index == self._pop_index:
            self._pop_index = (self._pop_index + 1) % self.capacity
        self._append_index = (self._append_index + 1) % self._capacity
        logger.debug('Performed append(). Container: "{}".'.format(self._container))

    def pop(self, index=None) -> Any:
        if index is not None:
            raise NotImplementedError

        logger.debug('Performing pop()...')
        logger.debug('append_index: "{}", pop_index: "{}", size: "{}"'.format(
            self._append_index, self._pop_index, self._capacity))

        index = self._pop_index

        try:
            value = self._container.pop(index)
        except KeyError as e:
            raise EmptyRingerException
        self._pop_index = (self._pop_index + 1) % self.capacity

        logger.debug('Performed pop(). Container: "{}", Extracted value: "{}".'.format(self._container, value))
        return value

    def __str__(self):
        return '{}(contents="{}", capacity="{}")'.format(self.__class__.__name__, self._container, self._capacity)
