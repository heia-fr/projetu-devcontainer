#!/usr/bin/env python3

import zipfile
import urllib.request

namespaces = "heia-fr"
project = "projetu-devcontainer"

req = urllib.request.Request(
    url="https://github.com/{namespace}/{project}/archive/refs/heads/main.zip"
)
with urllib.request.urlopen(req) as f:
    with zipfile.ZipFile(f) as z:
        print(z.namelist())
