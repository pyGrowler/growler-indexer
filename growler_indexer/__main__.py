#
# growler_indexer/__main__.py
#

import growler
from growler_indexer.middleware import Indexer

from argparse import ArgumentParser
from os import (stat, getcwd)
from sys import argv

cwd = getcwd()

aparser = ArgumentParser(prog='<prog>')
aparser.add_argument('--port', type=int, default=8989, help='Port server will listen on')
aparser.add_argument('--host', default='localhost', help='Port host will listen on')
aparser.add_argument('--prefix', default='', help='Prefix URL')
aparser.add_argument('dir', default= 'cwd', help='Directory to serve <Defaults Current>', nargs='*')
args = aparser.parse_args()

app = growler.App(__name__)
app.use(Indexer(args.dir))

app.run()

print ("MAIN", args.port)
