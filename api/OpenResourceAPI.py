import json
import requests
class OpenResourceAPI():
    def __init__(self):
        self.get_url = "http://10.106.0.93:8092/dmp-api/api/AutoModule/OpenResource"

    def OpenResource(self,session,resMD5):
        #准备参数
        data ={
                "userName":"xueyy",
                "MenuID":"{7B4707B7-0E93-4D3F-BD5E-12CDB76EB2A5}",
                "RuleID":"{61B5E1AC-4F39-43D1-AE98-C9D013F0ADCC}",
                # "resMD5":"4D0F7866B92D44193976ABB9E7BA0A20"
                "resMD5":resMD5
}
        #发送请求
        response = session.post(self.get_url,json=data)
        #返回响应
        return response

