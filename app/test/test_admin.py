# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/8 20:04
@Auth ： yongjie.su
@File ：test_admin.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
import requests
import unittest


class TestAdmin(unittest.TestCase):

    def setUp(self) -> None:
        url = 'http://127.0.0.1:8088/admin'
        self.query_url = url + '/query'
        self.add_url = url + '/add'

    def test_find(self):
        res = requests.post(self.query_url, params={"name": "test"})
        # print(res.content.decode('utf-8'))
        self.assertEqual(int(res.content.decode('utf-8')), 1)

    def test_add(self):
        data = {
            "name": "11",
            "phone": "11",
            "Ids": "11",
            "age": 10,
            "sex": "11",
            "org_id": 1,
            "org_name": "测试单位",
            "email": "11"
        }
        res = requests.post(self.add_url, json=data)
        self.assertEqual(int(res.content.decode('utf-8')), 1)


if __name__ == '__main__':
    unittest.main()
