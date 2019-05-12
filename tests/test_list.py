import unittest
from pathlib import Path

import ringer as rg


class TestRingerList(unittest.TestCase):

    def setUp(self) -> None:
        self.file_path = Path('test.rgr')

    def tearDown(self) -> None:
        self.file_path.unlink()

    def test_append(self):
        data = rg.RingerList(file_path=self.file_path, storage=rg.Storage.FILE)

        data.append('A')
        self.assertEqual(len(data), 1)

        data.append('B')
        self.assertEqual(len(data), 2)

        data.append('C')
        self.assertEqual(len(data), 3)

        data.append('D')
        self.assertEqual(len(data), 4)

    def test_pop(self):
        data = rg.RingerList(file_path=self.file_path, storage=rg.Storage.FILE, 
                             iterable=('A', 'B', 'C', 'D'))

        item = data.pop()
        self.assertEqual(item, 'D')

        item = data.pop()
        self.assertEqual(item, 'C')

        item = data.pop()
        self.assertEqual(item, 'B')

        item = data.pop()
        self.assertEqual(item, 'A')

        self.assertEqual(len(data), 0)


if __name__ == '__main__':
    unittest.main()
