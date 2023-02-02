#!/usr/bin/env python3

# Copyright (C) 2023 Jacques Supcik
# Haute école d'ingénierie et d'architecture de Fribourg
# SPDX-License-Identifier: Apache-2.0 or MIT

# Serve projetu website locally

import inotify.adapters
from pathlib import Path
import os
import shutil
from subprocess import call, Popen, PIPE
import signal
import sys
import logging

logging.basicConfig(level=logging.INFO)


def build(root):
    shutil.rmtree("./web", ignore_errors=True)
    src = []
    for root, _, files in os.walk(root, topdown=False):
        for name in files:
            if name.endswith(".md") and not name.startswith("README"):
                src.append(os.path.join(root, name))

    cmd = [
        "projetu-website-standalone",
        "--author",
        "Jacques Supcik",
        "--academic-year",
        "2022/2023",
        "--type",
        "ps6",
    ] + src

    return call(cmd)


def main():
    cwd = Path.cwd()

    os.chdir("/tmp")

    logging.info("cleaning...")
    shutil.rmtree("./public", ignore_errors=True)

    retcode = build(cwd)
    if retcode != 0:
        logging.error(f"Error building projetu : {retcode}")
        return

    p = Popen(["hugo", "serve", "-s", "./web"])

    def signal_handler(sig, frame):
        logging.warning()
        logging.warning("You pressed Ctrl+C!")
        logging.warning("Stopping hugo...")
        p.send_signal(signal.SIGINT)
        p.wait()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    logging.info("waiting for events...")

    i = inotify.adapters.InotifyTree(str(cwd))
    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event

        if filename == "FETCH_HEAD":
            continue

        if "IN_CLOSE_WRITE" in type_names:
            src = os.path.join(path, filename)
            logging.info(f"reloading ({src})")
            build(cwd)


if __name__ == "__main__":
    main()
