#!/usr/bin/env python
from __future__ import print_function
import sys, argparse, logging


__author__ = "Ori Jacobovitz"
__version__ = "1.0"


def main(args, loglevel):
    print("Program Started")
    logging.debug("Arguments: %s" % args)

    if args.interactive:
        interactive()

def interactive():
    help_message = """
    help - show this help message
    exit - quit from the program
    """

    commands = ['exit', 'help']
    exit = lambda: sys.exit()
    help = lambda: print(help_message)

    while True:
        cmd = raw_input('> ')
        if cmd in commands:
            eval(cmd + '()')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Script Description.")
    parser.add_argument(
        "arg1",
        help="argument number one",
        metavar="ARG1")
    parser.add_argument(
        "-v",
        "--verbose",
        help="increase output verbosity",
        action="store_true")
    parser.add_argument(
        "-i",
        "--interactive",
        help="run in interactive mode",
        action="store_true")

    args = parser.parse_args()

    if args.verbose:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.INFO

    logging.basicConfig(filename='template.log', format="%(asctime)s [%(levelname)s]: %(message)s", level=loglevel)

    main(args, loglevel)