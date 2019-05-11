import unittest

from ringer import \
    RingMemory, \
    EmptyRingException


class TestRingMemory(unittest.TestCase):

    def test_constructor(self):
        capacity = 5
        ring = RingMemory(capacity=capacity)
        self.assertEqual(ring.capacity, capacity)

    def test_append(self):
        ring = RingMemory(3)

        ring.append('A')
        self.assertEqual(len(ring), 1)

        ring.append('B')
        self.assertEqual(len(ring), 2)

        ring.append('C')
        self.assertEqual(len(ring), 3)

        ring.append('D')
        self.assertEqual(len(ring), 3)

    def test_pop(self):
        ring = RingMemory(3)

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

        self.assertRaises(EmptyRingException, ring.pop)


if __name__ == '__main__':
    unittest.main()
