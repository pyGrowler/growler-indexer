#
# growler_indexer/middleware.py
#

from os import (path)

class Indexer():
  
  def __init__(self, dir, prefix = "/"):
    print("[Indexer::__init__]")
    self.path = dir
    self.abs = path.abspath(dir)
    print("  hosting", self.abs)

  def __call__(self, req, res):
    res.send_html("<h1>%s</h1>" % (self.abs))
