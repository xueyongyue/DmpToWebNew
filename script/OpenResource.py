import logging
import unittest
import requests
import random
from parameterized import parameterized
from api.OpenResourceAPI import  OpenResourceAPI
import app
# from utils import read_param_data


class OpenResource(unittest.TestCase):

    def setUp(self) -> None:
        self.OpenResource_api =OpenResourceAPI()
        self.session = requests.Session()

    def tearDown(self) -> None:
        self.session.close()

    def test01_Add_MouduleRule_Success(self):
        response = self.OpenResource_api. OpenResource(self.session,resMD5='4D0F7866B92D44193976ABB9E7BA0A20' )
        print(response.json())
        logging.info("get tree code response = {}".format(response.json()))
        #对收到的响应结果，进行断言
        self.assertEqual(200,response.status_code)


