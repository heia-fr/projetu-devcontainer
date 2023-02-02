FROM ghcr.io/heia-fr/projetu:web

RUN pip install -U pip && pip install inotify
COPY ./serve.py /usr/local/bin/serve
RUN chmod +x /usr/local/bin/serve
