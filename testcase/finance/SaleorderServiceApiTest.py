#!/usr/bin/env pytho_*_ coding:utf-8 _*_

__author__ = 'dengyunpeng16605'

import grpc
import unittest
from grpcclient import Saleorder_pb2_grpc
from grpcclient import Saleorder_pb2

class SaleorderServiceApiTest(unittest.TestCase):
    def test_api(self):
        # 连接 rpc 服务器
        conn = grpc.insecure_channel("10.92.156.88:42241")
        # 调用 rpc 服务
        client = Saleorder_pb2_grpc.SaleorderServiceStub(channel = conn)
        response = client.PackageDetail(Saleorder_pb2.PackageDetailRequest(package_id=413053405425922))
        print(type(response))   #<class 'Saleorder_pb2.PackageDetailResponse'>
        print("SaleorderServiceStub:",response.package_aggregate_info.package_info.package_id)  #可强行打印出来，无法通过...快捷获取属性
        #校验
        self.assertIsNotNone(response.package_aggregate_info.package_info.package_id,"套餐详情为空")


if __name__ == '__main__':
    unittest.main()