growler-indexer
===============

Middleware for growler which generates an 'index view' of a directory.

This package can be imported to host specific directories on the server,
or can be called on the command line to create an easy file server for
quick access on a network.

On the command line, you can host the current directory on port 8000 using

`$ python3 -m growler_indexer`

In a webserver you use this module as:

```python

import growler
from growler_indexer.middleware import Indexer

app = growler.App(__name__)
app.use("/path1", Indexer("/path/to/be/served"))
app.use("/path2", Indexer("/another/path/to/be/served"))

...setup app...

app.run()

```
