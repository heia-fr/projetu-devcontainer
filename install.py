#!/usr/bin/env python3

# Copyright (c) 2021, Jacques Supcik
# Haute école d'ingénierie et d'architecture de Fribourg
# SPDX-License-Identifier: Apache-2.0 or MIT

# Devcontainer installer

import io
import os
import shutil
import urllib.request
import zipfile
from pathlib import Path, PurePosixPath

namespace = "heia-fr"
project = "projetu-devcontainer"


def main():

    if Path(".devcontainer").exists():
        print("Devcontainer already installed!")
        print("If you want to reinstall, remove the .devcontainer directory first.")
        return

    print("Installing devcontainer...")

    req = urllib.request.Request(
        url=f"https://github.com/{namespace}/{project}/archive/refs/heads/main.zip"
    )
    with urllib.request.urlopen(req) as f:
        with zipfile.ZipFile(io.BytesIO(f.read())) as z:
            for i in z.namelist():
                p = Path(i)
                if len(p.parts) < 3 or p.parts[1] != "devcontainer":
                    continue
                dst = PurePosixPath(".devcontainer").joinpath(*p.parts[2:])
                os.makedirs(dst.parent, exist_ok=True)
                with open(dst, "wb") as f:
                    shutil.copyfileobj(z.open(i), f)

    print(
        """Done.

You can now re-open this folder in a devcontainer.
The command "serve" will then serve the projetu website locally.

Enjoy !

-- Jacques
    """
    )


if __name__ == "__main__":
    main()
