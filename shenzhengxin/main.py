#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2023/03/29 13:18:11
@Author  :   SmallMu 
@Contact :   hunt_hak@outlook.com
@License :   (C)Copyright 2021-2022, WangShuai
'''
# https://webapi.cninfo.com.cn/#/marketDataDate
import requests
import time
import math
import base64
import execjs

time1 = math.floor(time.time())
mcode = base64.b64encode(str(time1).encode()).decode()
print(mcode)

with open("shenzhengxin/mcode.js", 'r', encoding="utf-8") as f:
    r = f.read()

ctx = execjs.compile(r).call("getResCode")
print(ctx)

cookies = {
    'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1680066919',
    'Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1680066939',
    'JSESSIONID': '9ABC4D7503A3004219BBFB3683257729',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh,en;q=0.9,zh-CN;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b=1680066919; Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b=1680066939; JSESSIONID=9ABC4D7503A3004219BBFB3683257729',
    'Origin': 'https://webapi.cninfo.com.cn',
    'Referer': 'https://webapi.cninfo.com.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'mcode': 'MTY4MDA2Njk1Mg==',
    'sec-ch-ua':
    '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'tdate': '2023-03-28',
    'market': 'SZE',
}

# response = requests.post(
#     'https://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007',
#     cookies=cookies,
#     headers=headers,
#     data=data)
# print(response.json())