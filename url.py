

class Url:

    def __init__(self, *args, **kwargs):
        j = kwargs.get('json', None)
        if j is not None:
            for key, value in j.items():
                setattr(self, key, value)
        else:
            self.url = kwargs.get('url', None)
            self.host = kwargs.get('host', None)
        print(self.__dict__)

    @property
    def dump(self):
        d = {}
        for key, val in self.__dict__.items():
            if key not in allowed_dump:
                d[key] = val
        return d
