import unittest
import app,time
from lib.HTMLTestRunner_PY3 import HTMLTestRunner
from script.GetTree import GetTree
from script.AddTreeNode import AddTreeNode
from script.UpdateTreeNode import UpdateTreeNode
from script.GetTable import GetTable
from script.AddMouduleRule import AddMouduleRule
from script.GetModuleRule import GetModuleRule
from script.DataTransform import DataTransform
from script.OpenResource import OpenResource
from script.RunModule import RunModule
from script.SaveData import SaveData
from script.UpdateModuleRule import UpdateModuleRule



suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(GetTree))
suite.addTest(unittest.makeSuite(AddTreeNode))
suite.addTest(unittest.makeSuite(UpdateTreeNode))
suite.addTest(unittest.makeSuite(AddMouduleRule))
suite.addTest(unittest.makeSuite(DataTransform))
suite.addTest(unittest.makeSuite(GetModuleRule))
suite.addTest(unittest.makeSuite(GetTable))
suite.addTest(unittest.makeSuite(OpenResource))
suite.addTest(unittest.makeSuite(RunModule))
suite.addTest(unittest.makeSuite(SaveData))
suite.addTest(unittest.makeSuite(UpdateModuleRule))
suite.addTest(unittest.makeSuite(UpdateTreeNode))




report_file = app.BASE_DIR + "/report/report{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
# report_file = app.BASE_DIR + "/report/report.html"
with open(report_file,'wb') as f:
    runner = HTMLTestRunner(f,title="入库web化项目接口测试报告",description="test")
    runner.run(suite)