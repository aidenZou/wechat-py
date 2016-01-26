import qrcode
# import pyqrcode
from tornado.web import RequestHandler
from conf.settings import log
from bin.util.helper import error, ErrorCode


class TestHandler(RequestHandler):
    def get(self):
        try:
            # img = qrcode.make('Some data here')
            # print(dir(img))
            #
            # print(img)

            # url = pyqrcode.create('http://m.baidu.com')
            # url.png('./a.png', quiet_zone=0, module_color=(0,128,0,255), background=(255, 255, 255, 0))

            # qr = qrcode.QRCode(
            #     version=1,
            #     error_correction=qrcode.constants.ERROR_CORRECT_L,
            #     box_size=10,
            #     border=0,
            # )
            # qr.add_data('http://m.baidu.com')
            # qr.make_image().show()

            # kwargs = (
            #     version=1,
            #     error_correction=qrcode.constants.ERROR_CORRECT_L,
            #     box_size=10,
            #     border=0,
            # )

            data = 'http://m.baidu.com'
            img = qrcode.make(data,
                              version=1,
                              error_correction=qrcode.constants.ERROR_CORRECT_L,
                              box_size=10,
                              border=0,
                              )

            img.show()

            res = {
                'code': 0
            }
            return self.write(res)
        except Exception as e:
            log.warn(e)

            return self.write(error(ErrorCode.SRVERR))
