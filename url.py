

class Url:

    def __init__(self, *args, **kwargs):
        print(args)
        print(kwargs)

if __name__ == '__main__':
    u = Url('', kwargs={'test': 100})