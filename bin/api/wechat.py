from tornado.web import RequestHandler
from bin.util.helper import error, ErrorCode
from conf.settings import log

from bin.service.wechat import Wechat


# 用户管理
class UserHandler(RequestHandler):
    # 获取微信用户信息
    async def get(self):
        try:
            id = int(self.get_argument('id'))
            openid_list = ['o3G9Ds5wc_j1TjSm_4ATvK86aCkI', 'o3G9Ds0FIEkBQaATmQM682dMel30']
            openid = openid_list[id]
        except Exception as e:
            log.warn(e)
            return self.write(error(ErrorCode.PARAMERR))

        try:
            wechat = Wechat()
            user_info = await wechat._get_user_info(openid)
            return self.write(user_info)
        except Exception as e:
            log.error(e)
            return self.write(error(ErrorCode.SRVERR))


# 用户列表
class UserListHandler(RequestHandler):
    # 获取微信用户信息
    async def get(self):
        try:
            wechat = Wechat()
            user_info = await wechat._get_user_list()
            return self.write(user_info)
        except Exception as e:
            log.error(e)
            return self.write(error(ErrorCode.SRVERR))


# 自定义菜单
class MenuHandler(RequestHandler):
    # 获取公众号菜单
    async def get(self):
        try:
            wechat = Wechat()
            menu_list = await wechat._get_menu()
            return self.write(menu_list)
        except Exception as e:
            log.error(e)
            return self.write(error(ErrorCode.SRVERR))


# 客服接口
class KfHandler(RequestHandler):
    async def get(self):
        try:
            wechat = Wechat()
            res = await wechat._kf_add()
            return self.write(res)
        except Exception as e:
            log.warn(e)
            return self.write(error(ErrorCode.SRVERR))


# 发送模板消息
class TemplateMessageHandler(RequestHandler):
    async def get(self):
        try:
            openid = 'oDCaswvE4Yp1urDqPAnAa4AAtznk'  # sqcyc 我
            # openid = 'oDCaswpr5LmDRejibnSddyxqfKzY' # sqcyc 利刚
            # openid = 'oDCaswuTKnQ607MzkVIYEYO8CDwU' # sqcyc 龙

            # 微信订单发货通知
            args = {
                "touser": openid,
                "template_id": "B6oWYamNIM4v498HncegGW5umO1Z78FnNWGYKjtDhHY",
                "url": "https://youcai.shequcun.com/#!/order",
                "data": {
                    "first": {
                        "value": "您好，您的订单已发货",
                        "color": "#173177"
                    },
                    "keyword1": {
                        "value": "100003456",
                        "color": "#173177"
                    },
                    "keyword2": {
                        "value": "顺丰快递",
                        "color": "#173177"
                    },
                    "keyword3": {
                        "value": "10000004567",
                        "color": "#173177"
                    },
                    "remark": {
                        "value": "点击查看订单详情。",
                        "color": "#173177"
                    }
                }
            }
            wechat = Wechat()
            res = await wechat._template_message_send(openid, args)
            return self.write(res)
        except Exception as e:
            log.warn(e)
            return self.write(error(ErrorCode.SRVERR))


# test
class TestHandler(RequestHandler):
    async def get(self):
        try:
            # wechat = Wechat()
            # res = await wechat._test()
            # return self.write(res)
            pass
        except Exception as e:
            log.warn(e)
            return self.write(error(ErrorCode.SRVERR))
