import requests

#定义获取业务节点树的类
class GetTreeAPI():
    def __init__(self):
        #接口的路径
        self.getTree_url ="http://10.106.0.93:8092//api/AutoModule/GetTree?userName=fanmj&menuType=30"

    def getTree(self, session):
        url=self.getTree_url
        #发送请求
        response = session.get(url)
        #返回响应
        return response
