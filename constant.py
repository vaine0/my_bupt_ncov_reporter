import os

USERS = eval(os.environ['USERS'])
SERVER_KEY = os.environ['SERVER_KEY']
BOT_TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = os.environ['CHAT_ID']


LOGIN_API = 'https://app.bupt.edu.cn/uc/wap/login/check'
GET_API = 'https://app.bupt.edu.cn/ncov/wap/default/index'
REPORT_API = 'https://app.bupt.edu.cn/ncov/wap/default/save'

# 当今日没有填报时，在https://app.bupt.edu.cn/ncov/wap/default/index下进行填报，
# 全部填完，不要提交，f12打开控制台，在Console页面下输入代码 console.log(vm.info) 就会得到以下信息，之后每天就默认填以下信息
# INFO = r"""{
#         "ismoved": 0,
#         "jhfjrq": "",
#         "jhfjjtgj": "",
#         "jhfjhbcc": "",
#         "sfxk": 0,
#         "xkqq": "",
#         "szgj": "",
#         "szcs": "",
#         "zgfxdq": "0",
#         "mjry": "0",
#         "csmjry": "0",
#         "ymjzxgqk": "接种2针",
#         "xwxgymjzqk": 3,
#         "uid": "24031",
#         "date": "20211121",
#         "tw": "3",
#         "sfcxtz": "0",
#         "sfyyjc": "0",
#         "jcjgqr": "0",
#         "jcjg": "",
#         "sfjcbh": "0",
#         "sfcxzysx": "0",
#         "qksm": "",
#         "remark": "",
#         "address": "北京市海淀区学院路街道志新村小区",
#         "area": "北京市  海淀区",
#         "province": "北京市",
#         "city": "北京市",
#         "geo_api_info": "{\"type\":\"complete\",\"info\":\"SUCCESS\",\"status\":1,\"dEa\":\"jsonp_289385_\",\"position\":{\"Q\":39.99014,\"R\":116.36657000000002,\"lng\":116.36657,\"lat\":39.99014},\"message\":\"Get ipLocation success.Get address success.\",\"location_type\":\"ip\",\"accuracy\":null,\"isConverted\":true,\"addressComponent\":{\"citycode\":\"010\",\"adcode\":\"110108\",\"businessAreas\":[{\"name\":\"牡丹园\",\"id\":\"110108\",\"location\":{\"Q\":39.977965,\"R\":116.37172700000002,\"lng\":116.371727,\"lat\":39.977965}}],\"neighborhoodType\":\"商务住宅;住宅区;住宅小区\",\"neighborhood\":\"志新村小区\",\"building\":\"\",\"buildingType\":\"\",\"street\":\"志新西路\",\"streetNumber\":\"49号\",\"country\":\"中国\",\"province\":\"北京市\",\"city\":\"\",\"district\":\"海淀区\",\"township\":\"学院路街道\"},\"formattedAddress\":\"北京市海淀区学院路街道志新村小区\",\"roads\":[],\"crosses\":[],\"pois\":[]}",
#         "created": 1637466883,
#         "sfzx": 1,
#         "sfjcwhry": "0",
#         "sfcyglq": "0",
#         "gllx": "",
#         "glksrq": "",
#         "jcbhlx": "",
#         "jcbhrq": "",
#         "sftjwh": "0",
#         "sftjhb": "0",
#         "fxyy": "开学",
#         "bztcyy": "",
#         "fjsj": "20211005",
#         "sfjchbry": "0",
#         "sfjcqz": "",
#         "jcqzrq": "",
#         "jcwhryfs": "",
#         "jchbryfs": "",
#         "xjzd": "",
#         "sfsfbh": 0,
#         "jhfjsftjwh": "0",
#         "jhfjsftjhb": "0",
#         "szsqsfybl": 0,
#         "sfygtjzzfj": 0,
#         "gtjzzfjsj": "",
#         "sfsqhzjkk": 0,
#         "sqhzjkkys": "",
#         "sfjzxgym": 1,
#         "sfjzdezxgym": 1,
#         "created_uid": 0,
#         "id": 15298473,
#         "gwszdd": "",
#         "sfyqjzgc": "",
#         "jrsfqzys": "",
#         "jrsfqzfy": ""
#         }"""
INFO = r'''{
        address: "新疆维吾尔自治区乌鲁木齐市天山区延安路街道富康街737号朗天峰景1期"
        area: "新疆维吾尔自治区 乌鲁木齐市 天山区"
        bztcyy: "4"
        city: "乌鲁木齐市"
        created: 1641351863
        created_uid: 0
        csmjry: "0"
        date: "20220105"
        fjsj: "20211005"
        fxyy: "开学"
        geo_api_info: "{\"type\":\"complete\",\"info\":\"SUCCESS\",\"status\":1,\"fEa\":\"jsonp_964714_\",\"position\":{\"Q\":43.76863,\"R\":87.64909999999998,\"lng\":87.6491,\"lat\":43.76863},\"message\":\"Get ipLocation success.Get address success.\",\"location_type\":\"ip\",\"accuracy\":null,\"isConverted\":true,\"addressComponent\":{\"citycode\":\"0991\",\"adcode\":\"650102\",\"businessAreas\":[],\"neighborhoodType\":\"\",\"neighborhood\":\"\",\"building\":\"\",\"buildingType\":\"\",\"street\":\"富康街\",\"streetNumber\":\"737号\",\"country\":\"中国\",\"province\":\"新疆维吾尔自治区\",\"city\":\"乌鲁木齐市\",\"district\":\"天山区\",\"towncode\":\"650102014000\",\"township\":\"延安路街道\"},\"formattedAddress\":\"新疆维吾尔自治区乌鲁木齐市天山区延安路街道富康街737号朗天峰景1期\",\"roads\":[],\"crosses\":[],\"pois\":[]}"
        glksrq: ""
        gllx: ""
        gtjzzfjsj: ""
        gwszdd: ""
        id: 16572767
        ismoved: 1
        jcbhlx: ""
        jcbhrq: ""
        jchbryfs: ""
        jcjg: ""
        jcjgqr: "0"
        jcqzrq: ""
        jcwhryfs: ""
        jhfjhbcc: ""
        jhfjjtgj: ""
        jhfjrq: ""
        jhfjsftjhb: "0"
        jhfjsftjwh: "0"
        jrsfqzfy: ""
        jrsfqzys: ""
        mjry: "0"
        province: "新疆维吾尔自治区"
        qksm: ""
        remark: ""
        sfcxtz: "0"
        sfcxzysx: "0"
        sfcyglq: "0"
        sfjcbh: "0"
        sfjchbry: "0"
        sfjcqz: ""
        sfjcwhry: "0"
        sfjzdezxgym: 1
        sfjzxgym: 1
        sfsfbh: 1
        sfsqhzjkk: 0
        sftjhb: "0"
        sftjwh: "0"
        sfxk: 0
        sfygtjzzfj: 0
        sfyqjzgc: ""
        sfyyjc: "0"
        sfzx: 0
        sqhzjkkys: ""
        szcs: ""
        szgj: ""
        szsqsfybl: 0
        tw: "3"
        uid: "24031"
        xjzd: "乌鲁木齐"
        xkqq: ""
        xwxgymjzqk: 3
        ymjzxgqk: "接种2针"
        zgfxdq: "0"
        }'''

REASONABLE_LENGTH = 24
TIMEOUT_SECOND = 25

class HEADERS:
    REFERER_LOGIN_API = 'https://app.bupt.edu.cn/uc/wap/login'
    REFERER_POST_API = 'https://app.bupt.edu.cn/ncov/wap/default/index'
    ORIGIN_BUPTAPP = 'https://app.bupt.edu.cn'

    UA = ('Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
          'Mobile/15E148 MicroMessenger/7.0.11(0x17000b21) NetType/4G Language/zh_CN')
    ACCEPT_JSON = 'application/json'
    ACCEPT_HTML = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    REQUEST_WITH_XHR = 'XMLHttpRequest'
    ACCEPT_LANG = 'zh-cn'
    CONTENT_TYPE_UTF8 = 'application/x-www-form-urlencoded; charset=UTF-8'

    def __init__(self) -> None:
        raise NotImplementedError

COMMON_HEADERS = {
    'User-Agent': HEADERS.UA,
    'Accept-Language': HEADERS.ACCEPT_LANG,
}
COMMON_POST_HEADERS = {
    'Accept': HEADERS.ACCEPT_JSON,
    'Origin': HEADERS.ORIGIN_BUPTAPP,
    'X-Requested-With': HEADERS.REQUEST_WITH_XHR,
    'Content-Type': HEADERS.CONTENT_TYPE_UTF8,
}

from typing import Optional
from abc import ABCMeta, abstractmethod

class INotifier(metaclass=ABCMeta):
    @property
    @abstractmethod
    def PLATFORM_NAME(self) -> str:
        """
        将 PLATFORM_NAME 设为类的 Class Variable，内容是通知平台的名字（用于打日志）。
        如：PLATFORM_NAME = 'Telegram 机器人'
        :return: 通知平台名
        """
    @abstractmethod
    def notify(self, *, success, msg, data,username, name) -> None:
        """
        通过该平台通知用户操作成功的消息。失败时将抛出各种异常。
        :param success: 表示是否成功
        :param msg: 成功时表示服务器的返回值，失败时表示失败原因；None 表示没有上述内容
        :return: None
        """

