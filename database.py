import os


class FileStorage:

    def __init__(self, *args, **kwargs):
        self.root = kwargs.get('root_folder', 'crawler_files\\')

    def __getitem__(self, item):
        if type(item) is str:
            return self.get_base(item)
        if type(item) is tuple:
            # must be host and url
            return self.get_direct(item)
        else:
            raise IndexError

    def __setitem__(self, key, value):
        pass
