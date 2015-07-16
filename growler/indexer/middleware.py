#
# growler/indexer/middleware.py
#

from os import (path, listdir)
from string import (Template)


class Indexer():
    """
    The main middleware class which does the file searching and the html
    rendering.
    """

    html_tmpl = Template("<!DOCTYPE html>"
                         "<html>"
                         "  <head>$head</head>"
                         "  <body>$body</body>"
                         "</html>")
    head_tmpl = Template("<title>$title</title>")

    def __init__(self, dir, prefix='/'):
        """
        Construct an Indexer middleware object, provided a directory to call
        and an optional http prefix.

        @param dir str: The path to the directory to serve.
        @param prefix str: The http prefix
        """
        print("[Indexer::__init__] (%s, %s)" % (dir, prefix))
        self.path = dir
        self.prefix = prefix
        self.abs = path.abspath(path.expanduser(dir))
        print("  hosting", self.abs)

    def __call__(self, req, res):
        """
        The middleware function for incoming requests. The path is split and
        explored.
        """
        tpath = path.join(self.abs, *req.path[1:].split('/'))
        print(req.protocol)
        print(req.headers, req.headers['host'])
        try:
            filenames = listdir(tpath)
        except FileNotFoundError:
            head = self.head_tmpl.substitute(title="404 Not Found")
            body = ("<h1>404 - Not Found</h1>"
                    "<p>The requested URL %s was not found on"
                    "this server.</p>") % (self.abs)
            res.send_html(self.html_tmpl.substitute(head=head, body=body), 404)
            return
        except Exception as e:
            print("ERRRR", e, tpath)
            res.send_file(tpath)
            return
        hostname = ''.join([req.headers['host'], req.path, '/'])
        filename_frmt = "<a href='http://%s{0}'>{1}</a>" % hostname
        filelinks = [filename_frmt.format(f) for f in filenames]
        ul = "<ul><li>%s</li></ul>" % ("</li><li>".join(filelinks))

        title = "Index of %s" % (self.path)
        body = "<h1>Index of %s</h1>%s" % (self.abs, ul)
        head = self.head_tmpl.substitute(title=title)
        res.send_html(self.html_tmpl.substitute(head=head, body=body))
