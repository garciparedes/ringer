import logging
from collections.abc import MutableSequence, Sequence
from pathlib import Path
from typing import Any, Iterable

from ..storages import Storage
from .base import Ringer

logger = logging.getLogger(__name__)


class RingerTuple(Ringer, Sequence):

    def __init__(self, file_path: Path, iterable: Iterable = None, *args, **kwargs):
        if kwargs.get('storage') != Storage.FILE:
            raise NotImplementedError

        super().__init__(*args, **kwargs)

        self._file_path = file_path

        with open(str(self._file_path), 'w') as file_writer:
            if iterable is not None:
                file_writer.writelines('{}\n'.format(value) for value in iterable)

    def __getitem__(self, index):
        logger.debug('Getting on "{}" index.'.format(index))
        with open(str(self._file_path)) as file_reader:
            return file_reader.readlines()[index].strip()

    def __len__(self):
        with open(str(self._file_path)) as f:
            return sum(1 for _ in f)


class RingerList(RingerTuple, MutableSequence):

    def insert(self, index: int, value: Any) -> None:
        logger.debug('Inserting "{}" on "{}" index.'.format(str(value)[:30], index))

        if self._file_path.exists():
            with open(str(self._file_path)) as file_reader:
                file_data = file_reader.readlines()
        else:
            file_data = list()
        raw_value = '{}\n'.format(value)
        file_data.insert(index, raw_value)

        with open(str(self._file_path), 'w') as file_writer:
            file_writer.writelines(file_data)

    def __setitem__(self, index, value):
        logger.debug('Setting "{}" on "{}" index.'.format(str(value)[:30], index))

        if self._file_path.exists():
            with open(str(self._file_path)) as file_reader:
                file_data = file_reader.readlines()
        else:
            file_data = list()
        raw_value = '{}\n'.format(value)
        file_data[index] = raw_value

        with open(str(self._file_path), 'w') as file_writer:
            file_writer.writelines(file_data)

    def __delitem__(self, index):
        logger.debug('Deleting on "{}" index.'.format(index))

        if self._file_path.exists():
            with open(str(self._file_path)) as file_reader:
                file_data = file_reader.readlines()
        else:
            file_data = list()
        del file_data[index]

        with open(str(self._file_path), 'w') as file_writer:
            file_writer.writelines(file_data)