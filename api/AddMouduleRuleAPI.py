import json
import requests
class AddMouduleRuleAPI():
    def __init__(self):
        self.getRule_url = "http://10.106.0.93:8092/dmp-api/api/AutoModule/AddModuleRule"

    def AddMouduleRule(self,session,MenuID,Caption1,PlatformType,TableName,Transaction,CommitCount,OperateType,Caption2,CreateUser):
        #准备参数
        data ={
                    "MenuID":MenuID,
                    "MatchRule":{

                    },
                    "FieldRule":[

                    ],
                    "Caption":Caption1,
                    "Message":"",
                    "PlatformType":PlatformType,
                    "TableRule":{
                        "TableName":TableName,
                        "Transaction":Transaction,
                        "CommitCount":CommitCount,
                        "OperateType":OperateType,
                        "Caption":Caption2
                    },
                    "CreateUser":CreateUser
                }
        #发送请求
        response = session.post(self.getRule_url,json=data)
        #返回响应
        return response

