import logging
import unittest
import requests
import random
from api.AddTreeNodeAPI import AddTreeNodeAPI
from utils import assert_utils
# 方法一
b=random.sample('abcdefghijklmnopqrstuvwxyz',2)
c=''.join(b)

a=random.randint(1,10)

class AddTreeNode(unittest.TestCase):

    def setUp(self) -> None:
        self.AddTreeNode_api =AddTreeNodeAPI()
        self.session = requests.Session()

    def tearDown(self) -> None:
        self.session.close()

    def test01_Add_Tree_Node1_Success(self):
        response = self.AddTreeNode_api.getTreeCode(self.session,ParentID='0',MenuType = '30',MenuName='测试模板'+str(a),Index='20',Level='1',OperatorUser = 'xueyy',BusinessCode = c )
        logging.info("get tree code response = {}".format(response.json()))
        #对收到的响应结果，进行断言
        self.assertEqual(200,response.status_code)

    def test02_Add_Tree_Node2_Success(self):
        response = self.AddTreeNode_api.getTreeCode(self.session,ParentID="{0605DC2B-F4EC-4DEE-8CF5-57131337EB5F}",MenuType = '30',MenuName= 'aesf',Index='0',Level='2',OperatorUser='xueyy',BusinessCode = "")
        logging.info("get tree code response = {}".format(response.json()))
        #对收到的响应结果，进行断言
        self.assertEqual(200,response.status_code)

    def test03_Add_Tree_Node3_Success(self):
        response = self.AddTreeNode_api.getTreeCode(self.session,ParentID="{77D340CF-94E7-4936-8E25-23DD668EFCFD}",MenuType = '30',MenuName= 'gfujjbg',Index='0',Level='3',OperatorUser='xueyy',BusinessCode = "")
        logging.info("get tree code response = {}".format(response.json()))
        #对收到的响应结果，进行断言
        self.assertEqual(200,response.status_code)