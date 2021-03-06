import os
import json
from host import Host
from url import Url


class FileStorage:

    def __init__(self, *args, **kwargs):
        self.root = kwargs.get('root_folder', 'crawler_files\\')

    def __getitem__(self, item):
        if type(item) is str:
            return self.get_host(item)
        if type(item) is tuple:
            # must be host and url (host, url)
            return self.get_url(item)
        else:
            raise TypeError

    def __setitem__(self, key, value):
        if type(item) is str:
            self.set_host(item, value)
        if type(item) is tuple:
            # must be host and url
            self.set_url(item, value)
        else:
            raise TypeError

    def get_host(self, host_str):
        with open(self.host_file(host_str), 'r') as file:
            return Host(json=json.load(file))

    def get_url(self, url_tuple):
        with open(self.url_file(url_tuple), 'r') as file:
            return Url(json=json.load(file))

    def set_host(self, host_str, value):
        assert type(value) is Host, 'Type must be Host'
        with open(self.host_file(host_str), 'r') as file:
            json.dump(file, value.dump)

    def set_url(self, url_tuple, value):
        assert type(value) is Url, 'Type must be Url'
        with open(self.url_file(url_tuple), 'r') as file:
            json.dump(file, value.dump)

    def url_file(self, url_tuple):
        f = self.root
        if not os.path.exists(f):
            os.mkdir(f)
        if not os.path.exists(os.path.join(f, url_tuple[0])):
            os.mkdir(os.path.join(f, url_tuple[0]))
        f = os.path.join(f, url_tuple[0], url_tuple[1])
        if not os.path.exists(f):
            os.mkdir(f)
        f = os.path.join(f, 'url_data.json')
        return f

    def host_file(self, host_str):
        f = self.root
        if not os.path.exists(f):
            os.mkdir(f)
        if not os.path.exists(os.path.join(f, host_str)):
            os.mkdir(os.path.join(f, host_str))
        f = os.path.join(f, host_str, 'host_data.json')
        return f


class Database:

    def __init__(self):
        pass


