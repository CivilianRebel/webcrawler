

class Host:

    def __init__(self, *args, **kwargs):
        self.host = kwargs.get('host', None)
        self.json = kwargs.get('json', None)
        if self.json is not None:
            for key, value in self.json.items():
                setattr(self, key, value)
