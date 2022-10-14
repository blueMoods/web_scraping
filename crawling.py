# python2
import sys
import argparse
import urllib2

def download(url, num_retries = 2, user_agent="BlueMoods"):
    print "Downloading:", url, "..."

    # Set agent
    # some web will reject the default agent: Python-urllib/2.7
    headers = {"User-agent": user_agent}
    request = urllib2.Request(url, headers=headers)

    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print "download error: ", e.reason
        html = None
        if num_retries > 0:
            # 5xx HTTP errors means that the error is happened on server
            # Retry it
            if hasattr(e, "code") and 500 <= e.code < 600:
                return download(url, num_retries -1)
    return html

class ArgumentParserNotExit(argparse.ArgumentParser):
    def error(self, message):
        self.print_usage(sys.stderr)
        raise ValueError('%s: error: %s\n'.format(self.prog, message))

def parse_args():
    parser = ArgumentParserNotExit()
    parser.add_argument("--url", "-u", type=str, default="http://httpstat.us/500",
                        help="The URL you want to crawling.")
    args = parser.parse_args()
    return args.url

def main():
    url = parse_args()
    html = download(url)
    # print html

if __name__ == '__main__':
    main()
