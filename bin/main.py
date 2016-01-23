import urllib.parse

import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options
from tornado.web import Application

from bin.api import *
from conf.settings import WECHAT_CFG

define("port", default=8000, help="run on the given port", type=int)
define('debug', default=False, help='debug mode', type=bool)


class IndexHandler(tornado.web.RequestHandler):
    async def get(self):
        ua = self.request.headers['User-Agent']
        hasWx = 'MicroMessenger' in ua

        # hasWx = False

        if hasWx:  # 微信
            code = self.get_argument('code', None)
            if not code:  # 没有 code 获取code
                # https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxf0e81c3bee622d60&redirect_uri=http%3A%2F%2Fnba.bluewebgame.com%2Foauth_response.php&response_type=code&scope=snsapi_userinfo&state=STATE#wechat_redirect
                api_url = 'https://open.weixin.qq.com/connect/oauth2/authorize?'
                redirect_uri = urllib.parse.quote(self.request.protocol + '://' + self.request.host)
                # redirect_uri = urllib.parse.quote('http://192.168.1.222:8050/')
                url = api_url + 'appid=' + WECHAT_CFG['appid'] \
                      + '&redirect_uri=' + redirect_uri \
                      + '&response_type=code&scope=snsapi_base' \
                      + '&state=aidenZou'
                return self.redirect(url)

        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')


class RouterWeb(Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),  # 首页

            # 微信API
            (r'/api/wechat_user', wechat.UserHandler),  # 用户
            (r'/api/wechat_menu', wechat.MenuHandler),  # 菜单
            (r'/api/wechat_kf', wechat.KfHandler),  # 客服
        ]

        settings = dict(
            debug=options.debug
        )
        super(RouterWeb, self).__init__(handlers, **settings)


def start():
    tornado.options.parse_command_line()

    # app = tornado.web.Application(handlers=[(r'/', IndexHandler)], debug=True)
    # http_server = tornado.httpserver.HTTPServer(app)
    # http_server.listen(options.port)

    RouterWeb().listen(options.port, xheaders=True)

    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    # tornado.options.parse_command_line()
    # # app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    # app = tornado.web.Application(handlers=[(r'/', IndexHandler)], debug=True)
    # http_server = tornado.httpserver.HTTPServer(app)
    # http_server.listen(options.port)
    # tornado.ioloop.IOLoop.instance().start()

    start()
