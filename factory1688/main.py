#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2023/03/29 08:58:17
@Author  :   SmallMu 
@Contact :   hunt_hak@outlook.com
@License :   (C)Copyright 2021-2022, WangShuai
'''
# https://factory.1688.com/index.html?scm=1028.1.1.20044
import requests
import execjs
import time

# d.token + '&' + i + '&' + g + '&' + c.data
token = "5995d572ae86c412c5acef1d547d98e3"
i = 1680053201875
i = round(time.time() * 1000)
g = "12574478"
c_data = '{"cid":"TpFacRecommendService:TpFacRecommendService","methodName":"execute","params":"{\\"pageNo\\":\\"2\\",\\"query\\":\\"\\",\\"pageSize\\":\\"20\\",\\"from\\":\\"PC\\",\\"showType\\":\\"transverse\\",\\"sort\\":\\"mix\\"}"}'
# c_data = '{"cid":"TpFacRecommendService:TpFacRecommendService","methodName":"execute","params":"{\\"pageNo\\":\\"1\\",\\"query\\":\\"\\",\\"pageSize\\":\\"20\\",\\"from\\":\\"PC\\",\\"showType\\":\\"transverse\\",\\"sort\\":\\"mix\\"}"}'

singKey = token + '&' + str(i) + '&' + g + '&' + c_data

headers = {
    'authority':
    'h5api.m.1688.com',
    'accept':
    '*/*',
    'accept-language':
    'zh,en;q=0.9,zh-CN;q=0.8',
    # 'cookie': '_m_h5_tk=c376d30ac00a9cedfca71bdf264a480f_1680010524272; _m_h5_tk_enc=23c398b9ab545129ef641f1eaebe4c32; cna=ac3tGJK8o3YCAXt5kdUC4Gti; cookie2=10be934dc9a56377acfdeddac10f140f; t=f9948e79208d7c300e0d10867cfd4c2f; _tb_token_=339ee37f3f4f5; __cn_logon__=false; xlly_s=1; alicnweb=touch_tb_at%3D1680002619319; l=fB_nRENHNxpXydiMBO5Churza77tPIOb8sPzaNbMiIEGa18ATNjFYNCs0HK97dtj_T5vwetP0_WjjdUBWu4U-E616C4W4mHyRCvw8eM3N7AN.; tfstk=cVK1B7Yee5V_Vmn0j1MeAhUO33SRaPwCHV1MCfPluP9K0-pN9s4U4_GZEEVA0tBC.; isg=BMrKpNtrmie-yhaLSkqr2IDCG7Bsu04Vnxu8sVQCXp0mB2vBPEkcJJExF3vb98at',
    'referer':
    'https://factory.1688.com/',
    'sec-ch-ua':
    '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile':
    '?0',
    'sec-ch-ua-platform':
    '"Windows"',
    'sec-fetch-dest':
    'script',
    'sec-fetch-mode':
    'no-cors',
    'sec-fetch-site':
    'same-site',
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    "cookie":
    "cna=ac3tGJK8o3YCAXt5kdUC4Gti; cookie2=10be934dc9a56377acfdeddac10f140f; t=f9948e79208d7c300e0d10867cfd4c2f; _tb_token_=339ee37f3f4f5; __cn_logon__=false; xlly_s=1; _m_h5_tk=5995d572ae86c412c5acef1d547d98e3_1680059358392; _m_h5_tk_enc=b3a8fb5018c86340d316ad55504bfb5b; alicnweb=touch_tb_at%3D1680051453103; tfstk=chwCBANaDeYQS0BkK2saC7BLgeHcaPts26g3Aw8Ea_Ay2GZEWsq23q_Fm7Y-U0n1.; l=fB_nRENHNxpXyp_8BO5alurza779BQAffsPzaNbMiIEGa1oh_afBINCsmZep8dtj_T5YCexP0_WjjdUBWP4LRE616C4W4mHyRj9p5eM3N7AN.; isg=BMzMnA2AxDyxSNDBGESFspIUnSr-BXCvrY36eyaPqXe4sWu7TBfCP19HUbGJ-agH"
}

with open("factory1688/sign.js", 'r', encoding="utf-8") as f:
    r = f.read()

ctx = execjs.compile(r).call('h', singKey)
print(ctx)

params = {
    'jsv': '2.6.1',
    'appKey': '12574478',
    't': str(i),
    'sign': ctx,
    'v': '1.0',
    'type': 'jsonp',
    'isSec': '0',
    'timeout': '20000',
    'api': 'mtop.taobao.widgetService.getJsonComponent',
    'dataType': 'jsonp',
    'jsonpIncPrefix': 'mboxfc',
    'callback': 'mtopjsonpmboxfc5',
    'data': c_data
}

response = requests.get(
    'https://h5api.m.1688.com/h5/mtop.taobao.widgetservice.getjsoncomponent/1.0/',
    params=params,
    # cookies=cookies,
    headers=headers,
)

print(response.text)
