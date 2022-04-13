import  logging
import unittest
import requests

from api.GetTablesAPI import  GetTablesAPI
from utils import assert_utils

class GetTable(unittest.TestCase):
    def setUp(self) -> None:
        self.get_Table = GetTablesAPI()
        self.session = requests.session()


    def tearDown(self) -> None:
        self.session.close()


    def test01_get_tree_success(self):
        response = self.get_Table.getTable(self.session)
        logging.info("get tree code response = {}".format(response.json()))
        self.assertEqual(200,response.status_code)
