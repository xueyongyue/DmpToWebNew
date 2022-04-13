import  logging
import unittest
import requests

from api.GetModuleRuleAPI import  GetModuleRuleAPI
from utils import assert_utils

class GetModuleRule(unittest.TestCase):
    def setUp(self) -> None:
        self.get_Rule = GetModuleRuleAPI()
        self.session = requests.session()


    def tearDown(self) -> None:
        self.session.close()


    def test01_get_tree_success(self):
        response = self.get_Rule.getRule(self.session)
        logging.info("get tree code response = {}".format(response.json()))
        self.assertEqual(200,response.status_code)