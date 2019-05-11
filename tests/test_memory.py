import unittest

import ringer as rg


class TestRingMemory(unittest.TestCase):

    def test_constructor(self):
        capacity = 5
        ring = rg.RingerDeque(capacity=capacity, storage=rg.Storage.MEMORY)
        self.assertEqual(ring.capacity, capacity)

    def test_append(self):
        ring = rg.RingerDeque(capacity=3, storage=rg.Storage.MEMORY)

        ring.append('A')
        self.assertEqual(len(ring), 1)

        ring.append('B')
        self.assertEqual(len(ring), 2)

        ring.append('C')
        self.assertEqual(len(ring), 3)

        ring.append('D')
        self.assertEqual(len(ring), 3)

    def test_pop(self):
        ring = rg.RingerDeque(capacity=3, storage=rg.Storage.MEMORY)

        ring.append('A')
        ring.append('B')
        ring.append('C')
        ring.append('D')

        result = ring.pop()
        self.assertEqual(result, 'B')

        result = ring.pop()
        self.assertEqual(result, 'C')

        result = ring.pop()
        self.assertEqual(result, 'D')

        self.assertRaises(rg.EmptyRingerException, ring.pop)


if __name__ == '__main__':
    unittest.main()
