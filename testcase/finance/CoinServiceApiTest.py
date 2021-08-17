#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'dengyunpeng16605'

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import unittest,requests,ddt
from config import Setting
from lib.ReadExcel import ReadExcel
from lib.SendRequests import SendRequests
# from lib.WriteExcel import

testData = ReadExcel(Setting.SOURCE_FILE, "c_new_service").read_data()

@ddt.ddt
class CoinServiceApiTest(unittest.TestCase):
    """虚拟币管理"""
    def setUp(self):
        self.s = requests.session()

    def tearDown(self):
        pass

    @ddt.data(*testData)
    def test_api(self,data):
        # 获取ID字段数值，截取结尾数字并去掉开头0
        # rowNum = int(data['ID'].split("_")[2])
        print("******* 正在执行用例 ->{0} *********".format(data['ID']))
        print("请求方式: {0}，请求URL: {1}".format(data['method'],data['url']))
        print("请求参数: {0}".format(data['params']))
        print("post请求body类型为：{0} ,body内容为：{1}".format(data['type'], data['body']))
        # 发送请求
        re = SendRequests().sendRequests(self.s,data)
        # 获取服务端返回的值
        self.result = re.json()
        print("页面返回信息：%s" % re.content.decode("utf-8"))
        # 获取excel表格数据的状态码和消息
        readData_code = int(data["status_code"])
        # readData_msg = data["msg"]
        # if readData_code == self.result['status'] and readData_msg == self.result['message']:
        #     OK_data = "PASS"
        #     print("用例测试结果:  {0}---->{1}".format(data['ID'],OK_data))
        #     WriteExcel(setting.TARGET_FILE).write_data(rowNum + 1,OK_data)
        # if readData_code != self.result['status'] or readData_msg != self.result['message']:
        #     NOT_data = "FAIL"
        #     print("用例测试结果:  {0}---->{1}", format(data['ID'], NOT_data))
        #     WriteExcel(setting.TARGET_FILE).write_data(rowNum + 1,NOT_data)
        self.assertEqual(self.result['ret'], readData_code, "返回实际结果是->:%s" % self.result['ret'])

if __name__=='__main__':
    unittest.main()
