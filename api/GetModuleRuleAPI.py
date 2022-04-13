import requests

#定义获取业务节点树的类
class GetModuleRuleAPI():
    def __init__(self):
        #接口的路径
        self.getRule_url ="http://10.106.0.93:8092/dmp-api/AutoModule/GetModuleRule?menuID=%7B1DBC38B6-3829-4421-80D2-59946825E8A6%7D"

    def getRule(self, session):
        url=self.getRule_url
        #发送请求
        response = session.get(url)
        #返回响应
        return response
