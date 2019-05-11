import logging

from ringer import RingMemory


def main():
    logging.basicConfig(level='DEBUG')

    ring = RingMemory(3)

    ring.append("A")
    ring.append("B")
    ring.append("C")
    ring.append("D")

    ring.pop()
    ring.pop()
    ring.append("E")
    ring.pop()
    ring.pop()
    ring.append("E")
    ring.append("F")
    ring.append("G")
    ring.append("H")

    ring.pop()

    print(ring)


if __name__ == '__main__':
    main()
