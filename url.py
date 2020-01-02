import json


class Url:

    def __init__(self, *args, **kwargs):
        self.url = kwargs.get('url', None)
        self.host = kwargs.get('host', None)
        self.json = kwargs.get('json', None)
        if self.json is not None:
            for key, value in self.json.items():
                setattr(self, key, value)


if __name__ == '__main__':
    u = Url(json=json.loads(json.dumps({'test': False, 'test2': 12})))