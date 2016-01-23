import urllib.parse
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

from util.wechat import Wechat

define("port", default=8000, help="run on the given port", type=int)
tornado.options.define('debug', default=False, help='debug mode', type=bool)

WXPAY_CONF = {
    'appid': 'wxb6f5a73e5c26cece',
    'appsecret': 'dc4f88a05170674d358c42be4eb1443a'
}


class IndexHandler(tornado.web.RequestHandler):
    async def get(self):
        ua = self.request.headers['User-Agent']
        hasWx = 'MicroMessenger' in ua

        if hasWx:  # 微信
            code = self.get_argument('code', None)
            if not code:  # 没有 code 获取code
                # https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxf0e81c3bee622d60&redirect_uri=http%3A%2F%2Fnba.bluewebgame.com%2Foauth_response.php&response_type=code&scope=snsapi_userinfo&state=STATE#wechat_redirect
                api_url = 'https://open.weixin.qq.com/connect/oauth2/authorize?'
                # redirect_uri = urllib.parse.quote(self.request.protocol + '://' + self.request.host)
                redirect_uri = 'http://114.254.129.181:8000/'
                url = api_url + 'appid=' + WXPAY_CONF['appid'] + \
                      '&response_type=code&scope=snsapi_base' \
                      '&redirect_uri=' + redirect_uri \
                      + '&state=aidenZou' \
                      + '&connect_redirect=1#wechat_redirect'
                return self.redirect(url)

        wechat = Wechat()
        res = await wechat._init()
        self.write(res)
        return

        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')


if __name__ == "__main__":
    tornado.options.parse_command_line()
    # app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    app = tornado.web.Application(handlers=[(r'/', IndexHandler)], debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
