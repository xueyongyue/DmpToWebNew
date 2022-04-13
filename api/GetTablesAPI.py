import requests

#定义获取业务节点树的类
class GetTablesAPI():
    def __init__(self):
        #接口的路径
        self.getTables_url ="http://10.106.0.93:8092/dmp-api/AutoModule/GetTables"

    def getTable(self, session):
        url=self.getTables_url
        #发送请求
        response = session.get(url)
        #返回响应
        return response
