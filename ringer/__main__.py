import argparse


def setup_parser():
    parser = argparse.ArgumentParser(prog='ringer')
    subparsers = parser.add_subparsers(help='sub-command help', metavar='COMMAND', dest='command', required=True)

    init_parser = subparsers.add_parser('enable', help='enable help')
    stop_parser = subparsers.add_parser('disable', help='disable help')
    list_parser = subparsers.add_parser('list', help='list help')

    add_parser = subparsers.add_parser('add', help='add help')
    add_parser.add_argument('path', help='path help')

    remove_parser = subparsers.add_parser('remove', help='remove help')
    remove_parser.add_argument('path', help='path help')

    edit_parser = subparsers.add_parser('edit', help='edit help')
    edit_parser.add_argument('path', help='path help')


    return parser


def main():
    parser = setup_parser()
    parser.parse_args()


if __name__ == '__main__':
    main()
