# python2
# -*- coding: utf-8 -*
#
import urllib2
import urlparse
import datetime
import time

class Throttle:
    """ Add a delay between downloads to the same domain
    """
    def __init__(self, delay):
        # amount of delay(seconds) between downloads for each domain
        self.delay = delay
        # timestamp of when a domain was last accessed
        self.domains = {}

    def wait(self, url):
        # get the domain of url
        domain = urlparse.urlparse(url).netloc
        last_accessed = self.domains.get(domain)

        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.datetime.now() - last_accessed).seconds
            if sleep_secs > 0:
                print "Waiting..."
                time.sleep(sleep_secs)

        self.domains[domain] = datetime.datetime.now()

s_throttle = Throttle(1)

def download(url = "http://httpstat.us/500", num_retries = 2, user_agent="BlueMoods"):
    s_throttle.wait(url)
    print "Downloading:", url, "..."

    # Set agent
    # some web will reject the default agent: Python-urllib/2.7
    headers = {"User-agent": user_agent}
    request = urllib2.Request(url, headers=headers)

    try:
        html = urllib2.urlopen(request).read()
        print "download success"
    except urllib2.URLError as e:
        print "download error: ", e.reason
        html = None
        if num_retries > 0:
            # 5xx HTTP errors means that the error is happened on server
            # Retry it
            if hasattr(e, "code") and 500 <= e.code < 600:
                return download(url, num_retries -1)
    return html
