import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh,en;q=0.9,zh-CN;q=0.8',
    'Connection': 'keep-alive',
    'From-Domain': '51job_web',
    'Origin': 'https://we.51job.com',
    'Referer': 'https://we.51job.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'partner': 'baidupz',
    'property': '%7B%22partner%22%3A%22baidupz%22%2C%22webId%22%3A2%2C%22fromdomain%22%3A%2251job_web%22%2C%22frompageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2F%22%2C%22pageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2Fpc%2Fsearch%3FjobArea%3D200200%26keyword%3Dpython%26searchType%3D2%26sortType%3D0%26metro%3D%22%2C%22identityType%22%3A%22%22%2C%22userType%22%3A%22%22%2C%22isLogin%22%3A%22%E5%90%A6%22%2C%22accountid%22%3A%22%22%7D',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sign': 'e00da68e29def3725757f940ed219792d8064884bd4318d9b822114396de2383',
    'uuid': '88485443d5f7b601cb5f3969b968252e',
}

params = {
    'api_key': '51job',
    'timestamp': '1679640671',
    'keyword': 'python',
    'searchType': '2',
    'function': '',
    'industry': '',
    'jobArea': '200200',
    'jobArea2': '',
    'landmark': '',
    'metro': '',
    'salary': '',
    'workYear': '',
    'degree': '',
    'companyType': '',
    'companySize': '',
    'jobType': '',
    'issueDate': '',
    'sortType': '0',
    'pageNum': '1',
    'requestId': '',
    'pageSize': '50',
    'source': '1',
    'accountId': '',
    'pageCode': 'sou|sou|soulb',
}

response = requests.get('https://cupid.51job.com/open/noauth/search-pc', params=params, headers=headers).json()
print(response)