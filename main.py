# python2
# -*- coding: utf-8 -*

import argparse
from crawling import *

class ArgumentParserNotExit(argparse.ArgumentParser):
    def error(self, message):
        self.print_usage(sys.stderr)
        raise ValueError('%s: error: %s\n'.format(self.prog, message))

def parse_args():
    parser = ArgumentParserNotExit()
    parser.add_argument("--url", "-u", type=str, default=" ",
                        help="The URL you want to crawling.")
    parser.add_argument("--regex", "-r", type=str, default=".*2021.*",
                        help="The link regex want to crawling.")
    args = parser.parse_args()
    return args

def main():
    url = parse_args().url
    regex = parse_args().regex

    if url.isspace():
        # crawl_sitmap()
        # crawl_id()
        crawl_link(link_regex = regex)
    else:
        # crawl_sitmap(url)
        # crawl_id(url)
        crawl_link(url, regex)


if __name__ == '__main__':
    main()
