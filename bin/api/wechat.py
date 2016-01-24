from tornado.web import RequestHandler
from bin.util.helper import error, ErrorCode
from bin.util.wechat import Wechat
from conf.settings import log


# 用户管理
class UserHandler(RequestHandler):
    # 获取微信用户信息
    async def get(self):
        try:
            id = int(self.get_argument('id'))
            # 利刚 我
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

    async def list(self):
        # TODO ...
        return self.write({'items': 333, 'slides': 444})


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
    pass