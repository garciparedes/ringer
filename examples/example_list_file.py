import logging
from pathlib import Path

from ringer import ListFile


def main():
    logging.basicConfig(level='DEBUG')

    file_path = Path('test.rgr')
    ring = ListFile(file_path)

    ring.append("A")
    ring.append("A")
    ring.append("A")
    ring.append("A")

    ring[1] = "B"
    ring[2] = "C"
    ring[3] = "D"

    print(ring[0])
    print(ring[1])
    print(ring[2])
    print(ring[3])


if __name__ == '__main__':
    main()
