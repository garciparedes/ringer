import unittest
from pathlib import Path

import ringer as rg


class TestRingerTuple(unittest.TestCase):

    def setUp(self) -> None:
        self.file_path = Path('test.rgr')

    def tearDown(self) -> None:
        self.file_path.unlink()

    def test_append(self):

        data = rg.RingerTuple(file_path=self.file_path, storage=rg.Storage.FILE, 
                              iterable=('A', 'B', 'C', 'D'))

        self.assertEqual('A', data[0])
        self.assertEqual('B', data[1])
        self.assertEqual('C', data[2])
        self.assertEqual('D', data[3])

        self.assertEqual(len(data), 4)


if __name__ == '__main__':
    unittest.main()
