# python2
# -*- coding: utf-8 -*
#
import urllib2

def download(url = "http://httpstat.us/500", num_retries = 2, user_agent="BlueMoods"):
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
