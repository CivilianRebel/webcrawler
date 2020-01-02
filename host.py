

class Host:

    def __init__(self, *args, **kwargs):
        self.host = kwargs.get('host', None)
        j = kwargs.get('json', None)
        if j is not None:
            for key, value in j.items():
                setattr(self, key, value)

    @property
    def dump(self):
        d = {}
        for key, val in self.__dict__.items():
            if key not in allowed_dump:
                d[key] = val
        return d
