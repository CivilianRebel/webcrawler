import os


class FileStorage:

    def __init__(self, *args, **kwargs):
        self.root = kwargs.get('root_folder', 'crawler_files\\')

    def __getitem__(self, item):
        if type(item) is str:
            return self.get_host(item)
        if type(item) is tuple:
            # must be host and url
            return self.get_url(item)
        else:
            raise TypeError

    def __setitem__(self, key, value):
        pass

    def get_host(self, host_str):
        with open(self.host_file(host_str), 'r') as file:
            return Host(json.load(file))

    def get_url(self, url_tuple):
        with open(self.url_file(url_tuple), 'r') as file:
            return Url(json.load(file))
