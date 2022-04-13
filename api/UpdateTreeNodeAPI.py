class UpdateTreeNodeAPI():
    def __init__(self):
        self.getTreeCode_url = "http://10.106.0.93:8092/dmp-api/api/AutoModule/UpdateTreeNode"
    def getTreeCode(self,session,ParentID,MenuType,MenuName,Index,Level,OperatorUser,BusinessCode):
        #准备参数
        data = {'ParentID': ParentID,'MenuType': MenuType ,'MenuName':MenuName,"Index":Index,
                "Level":Level,"OperatorUser":OperatorUser,"BusinessCode":BusinessCode}
        #发送请求
        response = session.post(self.getTreeCode_url,data=data)
        #返回响应
        return response