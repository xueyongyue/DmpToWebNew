import json
import requests
from requests import session


class AddMouduleRuleAPI():
    def __init__(self):
        self.getRule_url = "http://10.106.0.93:8092/dmp-api/api/AutoModule/AddModuleRule"

    def AddMouduleRule(self,session,MenuID,Caption1,PlatformType,TableName,Transaction,CommitCount,OperateType,Caption2,CreateUser):
        #准备参数
        # data = {'Caption': Caption,'CreateUser': CreateUser ,'FieldRule':FieldRule,"MatchRule":MatchRule,
        #         "MenuID":MenuID,"Message":Message,"PlatformType":PlatformType,
        #         "TableRule":{'Caption':Caption,'CommitCount':CommitCount,'OperateType':OperateType,'TableName':TableName,'Transaction':Transaction}}

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
        print(response.json())
        #返回响应
        return response
session = requests.Session()
a=AddMouduleRuleAPI()
b=a.AddMouduleRule(session,MenuID='{D82E69DC-DB8E-45F3-AB63-B314968CF0DB}',Caption1='测试',PlatformType='',TableName='usrABSCFSX',Transaction='true',CommitCount='500',OperateType='2',Caption2='ABS偿付顺序',CreateUser='xueyy')
print(b)