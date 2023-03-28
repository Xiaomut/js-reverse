import requests
import execjs

cookies = {
    'ASP.NET_SessionId': '3pgg5hazv1wqql3yhd50hku1',
}

e = {
    'pageNo': 1,
    'pageSize': 20,
    'total': 0,
    'AREACODE': '',
    'M_PROJECT_TYPE': '',
    'KIND': 'GCJS',
    'GGTYPE': '1',
    'PROTYPE': '',
    'timeType': '6',
    'BeginTime': '2022-09-20 00:00:00',
    'EndTime': '2023-03-20 23:59:59',
    'createTime': [],
    'ts': 1679298639214,
}

ctx = execjs.compile(open("fuzf/getsign.js", mode='r',
                          encoding='utf-8')).call('d', e)

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh,en;q=0.9,zh-CN;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'ASP.NET_SessionId=3pgg5hazv1wqql3yhd50hku1',
    'Origin': 'https://ggzyfw.fj.gov.cn',
    'Referer': 'https://ggzyfw.fj.gov.cn/business/list/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'portal-sign': '200a77eb9812756486da6fd520607be2',
    'sec-ch-ua':
    '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.post(
    'https://ggzyfw.fj.gov.cn/FwPortalApi/Trade/TradeInfo',
    cookies=cookies,
    headers=headers,
    json=e)
print(response.json())
