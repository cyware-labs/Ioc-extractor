import argparse
import os
from .text_factory import TextFactory


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')  # return an open file handle


def ioc_extractor():
    parser = argparse.ArgumentParser()

    # parser.add_argument("query", help="Fetch and find data from query data")
    parser.add_argument(
        '-u',
        '--url',
        dest='url',
        help='Specify the type of given query that is URL'
    )

    parser.add_argument("-f", '--file', dest="filename",
                        help="input file with text", metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))

    parser.add_argument('-d', '--defang', dest='defang',
                        action='store_true',
                        help="show defanged IOC data")

    args = parser.parse_args()
    TextFactory(args).run_command()
