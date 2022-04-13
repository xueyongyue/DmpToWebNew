import logging
import unittest
import requests
import random
from parameterized import parameterized
from api.AddMouduleRuleAPI import  AddMouduleRuleAPI
import app
# from utils import read_param_data


class AddMouduleRule(unittest.TestCase):

    def setUp(self) -> None:
        self.AddMouduleRule_api =AddMouduleRuleAPI()
        self.session = requests.Session()

    def tearDown(self) -> None:
        self.session.close()

    # @parameterized.expand(read_param_data("AddMouduleRule.json", "MenuID", "Caption1","PlatformType","CreateUser","TableRule","TableName,Transaction,CommitCount,OperateType,Caption2"))
    def test01_Add_MouduleRule_Success(self):
        response = self.AddMouduleRule_api.AddMouduleRule(self.session,MenuID='{D82E69DC-DB8E-45F3-AB63-B314968CF0DB}',Caption1='测试',PlatformType='',TableName='usrABSCFSX',Transaction='true',CommitCount='500',OperateType='2',Caption2='ABS偿付顺序',CreateUser='xueyy' )
        print(response.json())
        logging.info("get tree code response = {}".format(response.json()))
        #对收到的响应结果，进行断言
        self.assertEqual(200,response.status_code)


