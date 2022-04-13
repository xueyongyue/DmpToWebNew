import requests
class DeleteTreeNodeAPI():
    def __init__(self):
        self.DeleteTreeCode_url = "http://10.106.0.93:8092/dmp-api/api/AutoModule/DeleteTreeNode?MenuID={CCC1E018-B657-455E-9CA4-817F6D671478}"

    def DeleteTreeCode(self, session, MenuID):
        # 准备参数
        data = {'MenuID': MenuID}
        # 发送请求
        response = session.post(self.DeleteTreeCode_url, data=data)
        # 返回响应
        return response