import unittest

from ringer import RingMemory


class TestRingMemory(unittest.TestCase):

    def test_constructor(self):
        capacity = 5
        ring = RingMemory(capacity=capacity)
        self.assertEqual(ring.capacity, capacity)


if __name__ == '__main__':
    unittest.main()
