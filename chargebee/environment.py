from os import environ
import sys

py_major_v = sys.version_info[0]
py_minor_v = sys.version_info[1]

if py_major_v < 3:
    from urlparse import urlparse
elif py_major_v >= 3:
    from urllib.parse import urlparse


class Environment(object):

    chargebee_domain = None
    protocol= "https"
    API_VERSION = "v2"

    def __init__(self, options):
        self.api_key = options['api_key']
        self.site = options['site']

        proxy = urlparse(environ['HTTP_PROXY']) if 'HTTP_PROXY' in environ else None
        if proxy:
            self.proxy = proxy.hostname
            self.proxy_port = proxy.port
        else:
            self.proxy, self.proxy_port = None, None

        if self.chargebee_domain is None:
            self.api_endpoint = 'https://%s.chargebee.com/api/%s' % (self.site, self.API_VERSION)
        else:
            self.api_endpoint = 'http://%s.%s/api/%s' % (self.site, self.chargebee_domain, self.API_VERSION)

    def api_url(self, url):
        return self.api_endpoint + url
