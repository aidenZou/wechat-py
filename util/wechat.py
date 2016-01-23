import json
import urllib.parse
import logging
from tornado.httpclient import AsyncHTTPClient

logging.basicConfig(filename='../log/info.log', level=logging.DEBUG)

WXPAY_CONF = {
    'appid': 'wxb6f5a73e5c26cece',
    'appsecret': 'dc4f88a05170674d358c42be4eb1443a'
}


class Wechat:
    # 获取access token
    async def get_access_token(self):
        api_url = 'https://api.weixin.qq.com/cgi-bin/token?'
        # grant_type=client_credential&appid=APPID&secret=APPSECRET
        parameters = {
            'grant_type': 'client_credential',
            'appid': WXPAY_CONF['appid'],
            'secret': WXPAY_CONF['appsecret']
        }

        try:
            client = AsyncHTTPClient()
            response = await client.fetch(api_url + urllib.parse.urlencode(parameters))
            result = json.loads(response.body.decode())
            logging.info(result)
            # print(result)
            # log.error('code=%s ret=%s' % (code, result))

            if 'errcode' in result:  # error
                # {'errmsg': 'appid missing hint: [7Zuvya0541vr20]', 'errcode': 41002}
                print(result)
                pass
            else:  # success
                # {'expires_in': 7200, 'access_token': '_2-uahStyx6HWxkBH-euhmTR_nx7Xx7d-rX44MpViwN0gDILqpN7yNm-ZaWn0pC2ufP7B1jQX3DC2Mn0zK9N6pQic9jKvqPfgzJGLKa2U1oKSBcACATBK'}
                return result['access_token']

        except Exception as e:
            # log.error(e)
            # return self.write(error(ErrorCode.REQERR, '请求openid出错'))
            return 'error'

        return None

    async def _init(self):
        await self.get_access_token()
        return 'hello'
