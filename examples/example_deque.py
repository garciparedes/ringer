import logging

import ringer as rg


def main():
    logging.basicConfig(level='DEBUG')

    ring = rg.RingerDeque(capacity=3, storage=rg.Storage.MEMORY)

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
