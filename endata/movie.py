#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   movie.py
@Time    :   2023/03/28 17:21:50
@Author  :   SmallMu 
@Contact :   hunt_hak@outlook.com
@License :   (C)Copyright 2021-2022, WangShuai
'''
import requests
import execjs

# https://www.endata.com.cn/BoxOffice/BO/Year/index.html

cookies = {
    'gr_user_id': 'bc4a9509-0967-4ad1-b354-3a77c1e05e40',
}

headers = {
    'Accept': 'text/plain, */*; q=0.01',
    'Accept-Language': 'zh,en;q=0.9,zh-CN;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'gr_user_id=bc4a9509-0967-4ad1-b354-3a77c1e05e40',
    'Origin': 'https://www.endata.com.cn',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua':
    '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

for year in range(2008, 2024):
    data = {
        'year': f'{year}',
        'MethodName': 'BoxOffice_GetYearInfoData',
    }

    response = requests.post('https://www.endata.com.cn/API/GetData.ashx',
                             cookies=cookies,
                             headers=headers,
                             data=data)
    crypt_data = response.text

    with open("endata/movie.js", 'r', encoding="utf-8") as f:
        r = f.read()
    ctx = execjs.compile(r).call("webInstace.shell", crypt_data)
    print(ctx)