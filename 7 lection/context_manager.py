from functools import partial


class opened:
    def __init__(self, path, *args, **kwargs):
        self.opener = partial(open, path, *args, **kwargs)

    def __enter__(self):
        self.file = self.opener()
        return self.file

    def __exit__(self, *exc_info):
        self.file.close()
        del self.file



