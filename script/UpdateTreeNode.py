import logging
import unittest
import requests
from api.UpdateTreeNodeAPI import UpdateTreeNodeAPI
from utils import assert_utils
class UpdateTreeNode(unittest.TestCase):
    ParentID = "0"
    MenuType = "30"
    MenuName = "自动化测试模板1"
    Index = "20"
    Level = "1"
    OperatorUser = "xueyy"
    BusinessCode = "zd"
    def setUp(self) -> None:
        self.UpdateTreeNode_api =  UpdateTreeNodeAPI()
        self.session = requests.Session()

    def tearDown(self) -> None:
        self.session.close()

    def test01_Add_Tree_Node_Success(self):
        response = self.UpdateTreeNode_api.getTreeCode(self.session,self.ParentID,self.MenuType,self.MenuName,self.Index,self.Level,self.OperatorUser,self.BusinessCode)
        logging.info("get tree code response = {}".format(response.json()))
        #对收到的响应结果，进行断言
        self.assertEqual(200,response.status_code)