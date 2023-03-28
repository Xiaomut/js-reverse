#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2023/03/28 15:54:09
@Author  :   SmallMu 
@Contact :   hunt_hak@outlook.com
@License :   (C)Copyright 2021-2022, WangShuai
'''

import requests
import execjs

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh,en;q=0.9,zh-CN;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.qimingpian.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'sec-ch-ua':
    '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'page': '2',
    'num': '20',
    'sys': 'vip',
    'keywords': '',
    'unionid': '',
}

response = requests.post(
    'https://vipapi.qimingpian.cn/search/recommendedItemList',
    headers=headers,
    data=data)

encrypt_data = response.json()["encrypt_data"]
print(encrypt_data)

with open('qimingkeji/encrypt.js', 'r', encoding='utf-8') as f:
    r = f.read()

ctx = execjs.compile(r).call('s', encrypt_data)
print(ctx)