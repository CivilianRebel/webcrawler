

class Controller:

    def __init__(self, *args, **kwargs):
        self.seed_url = kwargs.get('seed_url', 'no_seed')
        self.nb_crawlers = kwargs.get('nb_crawlers', 1)
        self.nb_urls_per = kwargs.get('nb_urls_per_crawler', 10)
        self._running = False
        self.crawlers = list()
        self.database = Database()

    def init(self):
        # todo: there is more that needs to be done here
        host = self.database.get_host_list(self.nb_crawlers)
        for idx in range(self.nb_crawlers):
            c = Crawler(host=host[idx])
            self.crawlers.append(c)
        self._running = True

    @property
    def running(self):
        return self._running

    def set_seed(self, seed):
        self.seed_url = seed

    def start_crawl(self):
        [crawler.start() for crawler in self.crawlers]
        [crawler.join() for crawler in self.crawlers]