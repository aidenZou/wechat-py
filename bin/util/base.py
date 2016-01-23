from tornado.web import RequestHandler

from bin.util.helper import json_dumps


class BaseHandler(RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)

    def write(self, chunk):
        if isinstance(chunk, (dict, list, tuple)):
            if 'errcode' in chunk:
                self.errcode = chunk['errcode']

            chunk = json_dumps(chunk)
            self.set_header('Content-Type', 'application/json; charset=UTF-8')
            # self.set_header('Access-Control-Allow-Origin', '*')
            # self.set_header('Access-Control-Allow-Headers', 'X-Requested-With')
            self.response = chunk[:253] + '...' if len(chunk) > 256 else chunk
        else:
            ct = self._headers['Content-Type']
            if isinstance(ct, bytes):
                ct = ct.decode()

            self.response = '<%s>' % ct.split(';')[0]

        super(BaseHandler, self).write(chunk)
