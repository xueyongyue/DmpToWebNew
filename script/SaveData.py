import logging
import unittest
import requests
import random
from parameterized import parameterized
from api.SaveDataAPI import  SaveDataAPI
import app
# from utils import read_param_data


class SaveData(unittest.TestCase):

    def setUp(self) -> None:
        self.SaveData_api =SaveDataAPI()
        self.session = requests.Session()

    def tearDown(self) -> None:
        self.session.close()

    def test01_RunModule_Success(self):
        response = self.SaveData_api.SaveData(self.session,ResourceId="DEBE8A309D101979A754E1F0162ED2DB")
        print(response.json())
        logging.info("get tree code response = {}".format(response.json()))
        #对收到的响应结果，进行断言
        self.assertEqual(200,response.status_code)


