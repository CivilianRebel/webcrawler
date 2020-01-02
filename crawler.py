import requests as web
import bs4 as bs
import re
import multiprocessing


class Crawler(multiprocessing.Process):

    def __init__(self, *args, **kwargs):
        super(Crawler, self).__init__()
        self.host = kwargs.get('host', None)
        self.limit = kwargs.get('limit', None)
        if self.host is None:
            raise AttributeError
        if self.limit is None:
            raise AttributeError

    def run(self):
        database = Database()
        url_list = self.find_url_list(database)
        for url in url_list:
            print(str(url))
            resp = web.get(url.url)
            body = bs.BeautifulSoup(resp.text, 'lxml').body
            links = self.process_links(body)
            database.update_links(host=self.host, url=url, links=links)
            database.update_html(host=self.host, url=url, html=body.text)
            print(f'{self.host_hash}: {url.url_hash} html added, {len(links)} links found and processed')

    def find_url_list(self, database):
        urls = []
        for url in database.get_urls_by_host(self.host, self.limit):
            urls.append(url)
        return urls

