import  logging
import unittest
import requests

from api.DeleteTreeNodeAPI import DeleteTreeNodeAPI
from utils import assert_utils

class GetTree(unittest.TestCase):
    def setUp(self) -> None:
        self.deleteTree_api = DeleteTreeNodeAPI()
        self.session = requests.session()


    def tearDown(self) -> None:
        self.session.close()


    def test01_get_tree_delete(self):
        response = self.deleteTree_api.DeleteTreeCode(self.session, MenuID="%7BCCC1E018-B657-455E-9CA4-817F6D671478%7D")
        logging.info("get tree code response = {}".format(response.json()))
        # 对收到的响应结果，进行断言
        self.assertEqual(200, response.status_code)