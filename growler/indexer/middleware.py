#
# growler/indexer/middleware.py
#

from os import (path, listdir)

HTML_TMPL_STR = """
<!DOCTYPE html>
<html>
  <head>{head}</head>
  <body>{body}</body>
</html>
"""

HEAD_TMPL_STR = """
<meta charset=utf8>
<title>{title}</title>
"""

BODY_TMPL_STR = """
<h1>Index of {path}</h1>
<ul>{file_list}</ul>
"""

PATH_NOT_FOUND_ERR_BODY_TMPL_STR = """
<h1>404 - Not Found</h1>
<p>The requested URL '{path}' was not found on this server.</p>
"""

SERVER_ERROR_TMPL_STR = """
<h1>{error}</h1>
<p>{msg}</p>
"""


class Indexer():
    """
    The main middleware class which does the file searching and the html
    rendering.
    """

    def __init__(self, dir, prefix='/'):
        """
        Construct an Indexer middleware object, provided a directory to call
        and an optional http prefix.

        @param dir str: The path to the directory to serve.
        @param prefix str: The http prefix
        """
        print("[Indexer::__init__] dir=%s, prefix=%s" % (dir, prefix))
        self.path = dir
        self.prefix = prefix
        self.abs = path.abspath(path.expanduser(dir))
        print("  hosting", self.abs)

    def __call__(self, req, res):
        """
        The middleware function for incoming requests. The path is split and
        explored.
        """
        code = 200
        tpath = path.join(self.abs, *req.path[1:].split('/'))
        try:
            filenames = listdir(tpath)
        except FileNotFoundError:
            head = HEAD_TMPL_STR.format(title="404 Not Found")
            body = PATH_NOT_FOUND_ERR_BODY_TMPL_STR.format(path=self.abs)
            code = 404
        except NotADirectoryError:
            res.send_file(tpath)
            return
        except Exception as e:
            msg = "path '%s' returned the error '%s'" % (self.abs, e)
            head = HEAD_TMPL_STR.format(title="ERROR")
            body = SERVER_ERROR_TMPL_STR.format(error='500 - Server Error',
                                                msg=msg)
            code = 500
        else:
            hostname = (req.headers['HOST'], req.path)
            filename_frmt = "<a href='http://%s%s/{0}'>{0}</a>" % hostname
            filelinks = [filename_frmt.format(f) for f in filenames]
            file_list = "<li>%s</li>" % ("</li><li>".join(filelinks))

            title = "Index of %s" % (self.path)
            head = HEAD_TMPL_STR.format(title=title)
            body = BODY_TMPL_STR.format(path=self.abs, file_list=file_list)

        res.send_html(HTML_TMPL_STR.format(head=head, body=body), code)
