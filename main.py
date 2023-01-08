from blog import Blog

import logging, logging.config
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('app')

FILENAME = 'input.txt'

def main():
    logger.debug("start script.")
    with open(f'./{FILENAME}') as f:
        lines = f.read().splitlines()
    
    blog = Blog(lines)
    blog.build()
    logger.debug("end script.")

if __name__ == '__main__':
    main()
