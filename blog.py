import os
from article import Article

import logging, logging.config
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('app')

class Blog:
    BY_ARTICLE_LINE = '--------'
    BY_SECTION_LINE = '-----'
    OUTPUT_DIRECTORY = 'out/contents/posts'

    def __init__(self, lines: list[str]):
        # data structure
        self.articles = []
        # init temporary buffer 
        self.raw_articles = []
        self.raw_section_buffer = []
        self.raw_article_buffer = []
        # loads 
        self.__load_lines(lines)
        # convert
        self.__convert()

    def __load_lines(self, lines: list[str]):
        logger.debug("start load lines.")
        for line in lines:
            if line == self.BY_ARTICLE_LINE:
                self.__append_article()
            elif line == self.BY_SECTION_LINE:
                self.__append_section()
            else:
                self.__append_line(line)
        logger.debug("end load lines.")

    def __append_line(self, line: str):
        self.raw_section_buffer.append(line)

    def __append_section(self):
        self.raw_article_buffer.append(self.raw_section_buffer)
        self.raw_section_buffer = []

    def __append_article(self):
        self.raw_articles.append(self.raw_article_buffer)
        self.raw_article_buffer = []
    
    def __convert(self):
        logger.debug("start convert.")
        for raw_article in self.raw_articles:
            # parse metadata
            raw_meta_lines = raw_article[0]
            meta = {
                line.split(": ")[0]: line.split(": ")[1]
                for line in raw_meta_lines
            }

            # body excluded "BODY:"
            raw_article[1][0] = raw_article[1][0][5:]
            body = "\n".join(raw_article[1])

            article = Article(meta=meta, body=body)
            self.articles.append(article)
        logger.debug("end convert.")
    
    def build(self):
        logger.debug("start build.")
        for article in self.articles:
            filename = article.get_filename()
            self.__make_output_directory(f"{self.OUTPUT_DIRECTORY}/{filename}")
            with open(f"{self.OUTPUT_DIRECTORY}/{filename}", 'w') as f:
                f.write(article.get_hugo())
        logger.debug("end build.")

    def __make_output_directory(self, filename):
        path = os.path.dirname(filename)
        try:
            os.makedirs(path)
        except FileExistsError:
            pass