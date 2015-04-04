#
# growler/indexer/__main__.py
#

import growler
from growler.indexer.middleware import Indexer

from argparse import ArgumentParser
from os import (stat, getcwd)
from sys import argv

def main(args):

    cwd = getcwd()

    app = growler.App(__name__)
    app.use(Indexer(args.dir[0]))

    app.run()

if __name__ == '__main__':
    aparser = ArgumentParser(prog='<prog>')
    aparser.add_argument('--port', type=int, default=8989, help='Port server will listen on')
    aparser.add_argument('--host', default='localhost', help='Port host will listen on')
    aparser.add_argument('--prefix', default='', help='Prefix URL')
    aparser.add_argument('dir', default= 'cwd', help='Directory to serve <Defaults Current>', nargs='*')
    args = aparser.parse_args()

    sys.exit(main(args))
