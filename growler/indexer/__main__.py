#
# growler/indexer/__main__.py
#

import growler
from growler.indexer.middleware import Indexer

import sys
import os
from argparse import ArgumentParser


def parse_arguments(args):
    """
    Parses the arguments passed to the script using python's
    argparse.ArgumentParser.
    """
    parser = ArgumentParser(prog='growler.indexer')
    parser.add_argument('-p', '--port',
                        type=int,
                        default=8989,
                        help='Port server will listen on')
    parser.add_argument('-H', '--host',
                        default='localhost',
                        help='Port host will listen on')
    parser.add_argument('--prefix',
                        default='',
                        help='Prefix URL')
    parser.add_argument('dir',
                        default=os.getcwd(),
                        nargs='*',
                        help='Directory to serve <Defaults Current>')
    return parser.parse_args(args)


def main(argv):
    """
    Main function provided by the growler-indexer to allow python to execute
    the module.
    """
    args = parse_arguments(argv)

    app = growler.App(__name__)
    app.use(Indexer(args.dir[0]))

    app.create_server_and_run_forever(host=args.host, port=args.port)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
