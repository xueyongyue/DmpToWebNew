import json
import requests
class RunModuleAPI():
    def __init__(self):
        self.get_url = "http://10.106.0.93:8092/dmp-api/api/AutoModule/RunModule"

    def RunModule(self,session,MenuID):
        #准备参数
        data = {
            # "MenuID":"{F49D044E-9E07-4E5F-9CEA-D97C4C4F73A0}",
            "MenuID": MenuID,
            "RuleID":"{3E130CE1-AA58-43C7-B0AB-ACBC3A37C5D7}",
            "ResourceId":"DEBE8A309D101979A754E1F0162ED2DB"
}


        #发送请求
        response = session.post(self.get_url,json=data)
        #返回响应
        return response

