import os
from bin.util.logger import initlog

# ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# DEPLOY_PATH = os.path.dirname(ROOT_PATH)
# PROCESS_SN = os.path.basename(ROOT_PATH)
#
# print(DEPLOY_PATH)
#
# log = initlog({
#     'INFO': '%s/log/youcai-web-%s.info.log' % (DEPLOY_PATH, PROCESS_SN),
#     'NOTE': '%s/log/youcai-web-%s.note.log' % (DEPLOY_PATH, PROCESS_SN),
#     'ERROR': '%s/log/youcai-web-%s.error.log' % (DEPLOY_PATH, PROCESS_SN)
# }, mode='timed', backup_count=15)

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

db_file = {
    'access_token': '%s/db/db.txt' % ROOT_PATH,
}

log = initlog({
    'INFO': '%s/log/wechat-web.info.log' % ROOT_PATH,
    'NOTE': '%s/log/wechat-web.note.log' % ROOT_PATH,
    'WARN': '%s/log/wechat-web.warn.log' % ROOT_PATH,
    'ERROR': '%s/log/wechat-web.error.log' % ROOT_PATH
}, True, mode='timed', backup_count=15)

WECHAT_CFG = {
    'appid': 'wxb6f5a73e5c26cece',
    'appsecret': 'dc4f88a05170674d358c42be4eb1443a'
}
