import json
import urllib.parse
from tornado.httpclient import AsyncHTTPClient

from conf.settings import log, WECHAT_CFG, db_file


class Wechat:
    # access_token = ''

    async def _main(self):
        # await self._get_access_token()
        # await self._get_user_list()

        # {'openid': ['o3G9Ds5wc_j1TjSm_4ATvK86aCkI', 'o3G9Ds0FIEkBQaATmQM682dMel30']}
        # openid = 'o3G9Ds5wc_j1TjSm_4ATvK86aCkI'
        # user_info = await self._get_user_info(openid)
        return 'hello'


    # 获取access token
    async def _get_access_token(self):
        api_url = 'https://api.weixin.qq.com/cgi-bin/token?'
        parameters = {
            'grant_type': 'client_credential',
            'appid': WECHAT_CFG['appid'],
            'secret': WECHAT_CFG['appsecret']
        }

        access_token = ''
        with open(db_file['access_token'], mode="w+", encoding="UTF-8") as f:
            access_token = f.readline()
            f.close()

        if access_token:
            return access_token

        try:
            client = AsyncHTTPClient()
            response = await client.fetch(api_url + urllib.parse.urlencode(parameters))
            result = json.loads(response.body.decode())
            log.info(result)
            # log.error('code=%s ret=%s' % (code, result))

            if 'errcode' in result:  # error:{'errmsg': 'appid missing hint: [7Zuvya0541vr20]', 'errcode': 41002}
                # raise BaseException(result)
                raise
            else:  # success:{'expires_in': 7200, 'access_token': '_2-uahStyx6HWxkBH-euhmTR_nx7Xx7d-rX44MpViwN0gDILqpN7yNm-ZaWn0pC2ufP7B1jQX3DC2Mn0zK9N6pQic9jKvqPfgzJGLKa2U1oKSBcACATBK'}
                access_token = result['access_token']
                with open(db_file['access_token'], mode="w+", encoding="UTF-8") as f:
                    f.write(access_token)
                    f.close()
                return access_token

        except Exception as e:
            print(e)
            # log.error(e)
            # return self.write(error(ErrorCode.REQERR, '请求openid出错'))
            raise


    # 获取用户列表
    # http://mp.weixin.qq.com/wiki/12/54773ff6da7b8bdc95b7d2667d84b1d4.html
    async def _get_user_list(self):
        api_url = 'https://api.weixin.qq.com/cgi-bin/user/get?'
        parameters = {
            'access_token': await self._get_access_token(),
            'next_openid': ''
        }

        try:
            client = AsyncHTTPClient()
            response = await client.fetch(api_url + urllib.parse.urlencode(parameters))
            result = json.loads(response.body.decode())
            # {'data': {'openid': ['o3G9Ds5wc_j1TjSm_4ATvK86aCkI', 'o3G9Ds0FIEkBQaATmQM682dMel30']}, 'total': 2, 'count': 2, 'next_openid': 'o3G9Ds0FIEkBQaATmQM682dMel30'}

            log.info(result)

            print(result)

            if 'errcode' in result:  # error:{'errmsg': 'appid missing hint: [7Zuvya0541vr20]', 'errcode': 41002}
                log.error(result)
                raise
            else:  # success:{'expires_in': 7200, 'access_token': '_2-uahStyx6HWxkBH-euhmTR_nx7Xx7d-rX44MpViwN0gDILqpN7yNm-ZaWn0pC2ufP7B1jQX3DC2Mn0zK9N6pQic9jKvqPfgzJGLKa2U1oKSBcACATBK'}
                # 'data': {'openid': ['o3G9Ds5wc_j1TjSm_4ATvK86aCkI', 'o3G9Ds0FIEkBQaATmQM682dMel30']}

                if result['count']:
                    for openid in result['data']['openid']:
                        print(openid)
                        # user = await self._get_user_info(openid)
                        # log.info('%s' % user)
                        # log.info('%s' % user.encode())
                        # print('%s' % user)

                return result

        except Exception as e:
            log.error(e)
            # return self.write(error(ErrorCode.REQERR, '请求openid出错'))
            raise

    # 获取用户基本信息(UnionID机制)
    # http://mp.weixin.qq.com/wiki/1/8a5ce6257f1d3b2afb20f83e72b72ce9.html
    async def _get_user_info(self, openid):
        if not openid:
            raise

        api_url = 'https://api.weixin.qq.com/cgi-bin/user/info?'
        parameters = {
            'access_token': await self._get_access_token(),  # 调用接口凭证
            'openid': openid,  # 普通用户的标识，对当前公众号唯一
            'lang': 'zh_CN'  # 返回国家地区语言版本，zh_CN 简体，zh_TW 繁体，en 英语
        }

        try:
            client = AsyncHTTPClient()
            response = await client.fetch(api_url + urllib.parse.urlencode(parameters))  # 返回JSON数据包给公众号

            result = response.body.decode()
            log.info('%s' % result.encode())

            result = json.loads(result)
            if 'errcode' in result:  # error:{'errmsg': 'appid missing hint: [7Zuvya0541vr20]', 'errcode': 41002}
                raise
            else:  # success:
                return result

        except Exception as e:
            # log.error(e)
            # return self.write(error(ErrorCode.REQERR, '获取用户基本信息(UnionID机制) error'))
            raise

    # 自定义菜单查询接口
    # http://mp.weixin.qq.com/wiki/5/f287d1a5b78a35a8884326312ac3e4ed.html
    async def _get_menu(self):
        api_url = 'https://api.weixin.qq.com/cgi-bin/menu/get?'
        parameters = {
            'access_token': await self._get_access_token()  # 调用接口凭证
        }

        try:
            client = AsyncHTTPClient()
            response = await client.fetch(api_url + urllib.parse.urlencode(parameters))  # 返回JSON数据包给公众号

            result = response.body.decode()
            log.info('%s' % result.encode())

            result = json.loads(result)
            if 'errcode' in result:  # error:{"errcode":46003,"errmsg":"menu no exist hint: [3v4USA0447vr21]"}
                if result['errcode'] in [46003]:
                    return result
                raise
            # success:
            return result

        except Exception as e:
            # log.error(e)
            # return self.write(error(ErrorCode.REQERR, '获取用户基本信息(UnionID机制) error'))
            raise

    # 自定义菜单创建接口
    # http://mp.weixin.qq.com/wiki/10/0234e39a2025342c17a7d23595c6b40a.html
    async def _set_menu(self):
        access_token = await self._get_access_token()
        api_url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=' + access_token
        parameters = {
            "button": [
                {
                    "type": "click",
                    "name": "今日歌曲",
                    "key": "V1001_TODAY_MUSIC"
                },
                {
                    "name": "菜单",
                    "sub_button": [
                        {
                            "type": "view",
                            "name": "搜索",
                            "url": "http://www.soso.com/"
                        },
                        {
                            "type": "view",
                            "name": "视频",
                            "url": "http://v.qq.com/"
                        },
                        {
                            "type": "click",
                            "name": "赞一下我们",
                            "key": "V1001_GOOD"
                        }]
                }]
        }

        try:
            client = AsyncHTTPClient()
            # response = await client.fetch(api_url, 'POST')  # 返回JSON数据包给公众号

            # response = await client.fetch(api_url, handle_request=None, method='POST', headers=None, body=parameters)
            response = await client.fetch(api_url, method='POST',
                                          body=json.dumps(parameters, ensure_ascii=False).encode(encoding='utf-8'))
            result = response.body.decode()
            print(result)

            log.info('%s' % result.encode())

            return result

        except Exception as e:
            log.error(e)
            # return self.write(error(ErrorCode.REQERR, '获取用户基本信息(UnionID机制) error'))
            raise

    # 客服管理
    # http://mp.weixin.qq.com/wiki/18/749901f4e123170fb8a4d447ae6040ba.html

    # 添加客服帐号
    async def _kf_add(self):
        access_token = await self._get_access_token()
        api_url = 'https://api.weixin.qq.com/customservice/kfaccount/add?access_token=' + access_token
        parameters = {
            # 'kf_account': 'hello@gh_de1d507e15d1',  # 完整客服账号，格式为：账号前缀@公众号微信号
            'kf_account': 'z_guilin@公众号微信号',  # 完整客服账号，格式为：账号前缀@公众号微信号
            'nickname': 'hello',
            'password': 'pswmd5',
        }
        body = json.dumps(parameters, ensure_ascii=False).encode(encoding='utf-8')

        try:
            client = AsyncHTTPClient()
            response = await client.fetch(api_url, method='POST', body=body)
            result = response.body.decode()
            print(result)

            log.info('%s' % result.encode())

            return result

        except Exception as e:
            log.error(e)
            # return self.write(error(ErrorCode.REQERR, '获取用户基本信息(UnionID机制) error'))
            raise

    # 模板消息接口
    # http://mp.weixin.qq.com/wiki/17/304c1885ea66dbedf7dc170d84999a9d.html
    # 发送模板消息
    async def _template_message_send(self, openid, args):
        access_token = await self._get_access_token()
        api_url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=' + access_token
        body = json.dumps(args, ensure_ascii=False).encode(encoding='utf-8')

        try:
            client = AsyncHTTPClient()
            response = await client.fetch(api_url, method='POST', body=body)
            result = response.body.decode()
            print(result)

            log.info('%s' % result.encode())

            return result

        except Exception as e:
            log.error(e)
            # return self.write(error(ErrorCode.REQERR, '获取用户基本信息(UnionID机制) error'))
            raise
