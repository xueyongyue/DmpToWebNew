import json
import requests
class SaveDataAPI():
    def __init__(self):
        self.get_url = "http://10.106.0.93:8092/dmp-api/api/AutoModule/SaveData"

    def SaveData(self,session,ResourceId):
        #准备参数
        data ={
    # "ResourceId":"DEBE8A309D101979A754E1F0162ED2DB",
    "ResourceId": ResourceId,
    "MenuID":"{F49D044E-9E07-4E5F-9CEA-D97C4C4F73A0}",
    "RuleID":"{3E130CE1-AA58-43C7-B0AB-ACBC3A37C5D7}",
    "TableRule":{
        "TableName":"usrLCCPJBXXB",
        "Caption":"理财产品基本信息表",
        "DataMode":0,
        "OperateType":2,
        "Formulas":[

        ],
        "TargetFormulas":[

        ],
        "FilterRows":[

        ],
        "LastFormulas":[

        ],
        "Uniques":[
            "CPDM"
        ],
        "CommitCount":500,
        "Transaction":"true",
        "AllConver":"false",
        "GKBZ":"false",
        "BulkSave":"false",
        "RetrySave":"false",
        "Distinct":"false",
        "OverwriteLaborData":"false",
        "ZeroEqualNull":"false",
        "ExtendData":"",
        "ReloadDB":"false"
    }
}
        #发送请求
        response = session.post(self.get_url,json=data)
        #返回响应
        return response

