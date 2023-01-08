import datetime 

import logging, logging.config
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('app')

from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader('templates'),
    trim_blocks=True
)

class Article:
    def __init__(self, meta, body):
        self.meta = meta
        self.body = body

    def get_title(self):
        return self.meta['TITLE']
    
    def get_filename(self):
        date_str = self.meta['DATE']
        date = datetime.datetime.strptime(date_str, '%m/%d/%Y %H:%M:%S')
        return date.strftime('%Y/%m/%d/%H%M%S.md')

    def get_date(self):
        date_str = self.meta['DATE']
        date = datetime.datetime.strptime(date_str, '%m/%d/%Y %H:%M:%S')
        return date.strftime('%Y-%m-%dT%H:%M:%S+09:00')

    def get_body(self):
        return self.body
 
    def get_hugo(self):
        template = env.get_template('hugo.jinja')
        result = template.render(
            title=self.get_title(), 
            date=self.get_date(),
            body=self.get_body(),
        )
        return result
