import logging
import unittest
import requests
import random
from parameterized import parameterized
from api.DataTransformAPI import  DataTransformAPI
import app
# from utils import read_param_data


class DataTransform(unittest.TestCase):

    def setUp(self) -> None:
        self.DataTransform_api =DataTransformAPI()
        self.session = requests.Session()

    def tearDown(self) -> None:
        self.session.close()

    def test01_Add_DataTransform_Success(self):
        response = self.DataTransform_api.DataTransform(self.session,CPDM='2021' )
        print(response.json())
        logging.info("get tree code response = {}".format(response.json()))
        #对收到的响应结果，进行断言
        self.assertEqual(200,response.status_code)


