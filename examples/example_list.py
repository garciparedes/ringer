import logging
from pathlib import Path

import ringer as rg


def main():
    logging.basicConfig(level='DEBUG')

    file_path = Path('test.rgr')
    ring = rg.RingerList(file_path=file_path, storage=rg.Storage.FILE)

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
