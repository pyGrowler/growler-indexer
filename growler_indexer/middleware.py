#
# growler_indexer/middleware.py
#

from os import (path, listdir)
from string import (Template)


class Indexer():
  
  html_tmpl = Template("""<!DOCTYPE html><html><head>$head</head><body>$body</body></html>""")
  head_tmpl = Template("""<title>$title</title>""")
  
  def __init__(self, dir, prefix = "/"):
    print("[Indexer::__init__]")
    self.path = dir
    print("dir:",dir)
    print (path.expanduser(dir))
    self.abs = path.abspath(path.expanduser(dir))
    print("  hosting", self.abs)

  def __call__(self, req, res):
    tpath = path.join(self.abs, *req.path[1:].split('/'))
    print (req.protocol)
    print (req.headers, req.headers['host'])
    try:
      filenames = listdir(tpath)
    except FileNotFoundError:
      head = self.head_tmpl.substitute(title="404 Not Found")
      body = "<h1>404 - Not Found</h1><p>The requested URL %s was not found on this server." % (self.abs)
      res.send_html(self.html_tmpl.substitute(head=head, body=body), 404)
      return
    except Exception as e:
      print ("ERRRR", e,tpath)
      res.send_file(tpath)
      return

    filelinks = ["<a href='{0}'>{1}</a>".format('http://' + req.headers['host'] + req.path + '/' + f, f) for f in filenames]    
    ul = "<ul><li>%s</li></ul>" % ("</li><li>".join(filelinks))

    title = "Index of %s" % (self.path)
    body = "<h1>Index of %s</h1>%s" % (self.abs, ul)
    head = self.head_tmpl.substitute(title=title)
    res.send_html(self.html_tmpl.substitute(head=head, body=body))
