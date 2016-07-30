import sys
import argparse

if __name__ == '__main__':
    print __file__
    parser = argparse.ArgumentParser(prog='recipe')
    parser.add_argument('--foo', action='store_true', help='foo help')
    subparsers = parser.add_subparsers(help='sub-command help', dest='command')
    parser_a = subparsers.add_parser('startproject', help='startproject help')
    parser_a.add_argument('bar', type=int, help='bar help')

    parser_b = subparsers.add_parser('list', help='list help')
    parser_b.add_argument('bar', type=int, help='bar help')
    parser_b.add_argument('-f', '--foo', type=int, help='bar help')

    args = parser.parse_args(['--foo', 'list', '12'])
    print(args)
    print sys.argv
    parser.print_help()
