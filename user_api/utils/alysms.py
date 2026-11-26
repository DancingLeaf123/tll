import os
from alibabacloud_dysmsapi20170525.client import Client as Dysmsapi20170525Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dysmsapi20170525 import models as dysmsapi_20170525_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from .single import SingletonMeta
import json


class AliyunSMSSender(metaclass=SingletonMeta):
    template_code = "SMS_154950909"
    sign_name = "阿里云短信测试"
    def __init__(self):
        ak = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_ID')
        sk = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_SECRET')
        if not ak or not sk:
            self.client = None
            return
        config = open_api_models.Config(
            access_key_id=ak,
            access_key_secret=sk
        )
        config.endpoint = f'dysmsapi.aliyuncs.com'
        self.client = Dysmsapi20170525Client(config)

    async def send_code(self, mobile, code: str):
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(
            phone_numbers=mobile,
            sign_name=self.sign_name,
            template_code=self.template_code,
            template_param=json.dumps({'code': code})
        )
        try:
            # 复制代码运行请自行打印 API 的返回值
            response = await self.client.send_sms_with_options_async(send_sms_request, util_models.RuntimeOptions())
            print(response)
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)