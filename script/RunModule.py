import logging
import unittest
import requests
import random
from parameterized import parameterized
from api.RunModuleAPI import  RunModuleAPI
import app
# from utils import read_param_data


class RunModule(unittest.TestCase):

    def setUp(self) -> None:
        self.RunModule_api =RunModuleAPI()
        self.session = requests.Session()

    def tearDown(self) -> None:
        self.session.close()

    def test01_RunModule_Success(self):
        response = self.RunModule_api.RunModule(self.session,MenuID="{F49D044E-9E07-4E5F-9CEA-D97C4C4F73A0}" )
        print(response.json())
        logging.info("get tree code response = {}".format(response.json()))
        #对收到的响应结果，进行断言
        self.assertEqual(200,response.status_code)


