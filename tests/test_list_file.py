import unittest
from pathlib import Path

from ringer import ListFile


class TestRingMemory(unittest.TestCase):

    def setUp(self) -> None:
        self.file_path = Path('test.rgr')
        self.ring = ListFile(file_path=self.file_path)

    def tearDown(self) -> None:
        self.file_path.unlink()

    def test_append(self):
        self.ring.append('A')
        self.assertEqual(len(self.ring), 1)

        self.ring.append('B')
        self.assertEqual(len(self.ring), 2)

        self.ring.append('C')
        self.assertEqual(len(self.ring), 3)

        self.ring.append('D')
        self.assertEqual(len(self.ring), 4)

    def test_pop(self):
        self.ring.append('A')
        self.ring.append('B')
        self.ring.append('C')
        self.ring.append('D')

        result = self.ring.pop()
        self.assertEqual(result, 'D')

        result = self.ring.pop()
        self.assertEqual(result, 'C')

        result = self.ring.pop()
        self.assertEqual(result, 'B')

        result = self.ring.pop()
        self.assertEqual(result, 'A')

        self.assertEqual(len(self.ring), 0)


if __name__ == '__main__':
    unittest.main()
