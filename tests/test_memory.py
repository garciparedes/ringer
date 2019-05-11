import unittest

from ringer import RingMemory


class TestRingMemory(unittest.TestCase):

    def test_constructor(self):
        size = 5
        ring = RingMemory(size=size)
        self.assertEqual(ring.size, size)


if __name__ == '__main__':
    unittest.main()
