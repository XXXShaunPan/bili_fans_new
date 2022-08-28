import requests
import time,sys
from datetime import datetime
import rob_login,wx_message


api_url='https://apim.yxshiyong.com/home/my/Signin'

data={'token':''}

header={'content-type':'application/json;charseT=UTF-8',
	'cookie':'__jsluid_s=6acc37734674965943c62a9c9800149b',
	'host':'apim.yxshiyong.com',
	'origin':'https://m.yxshiyong.com',
	'pragma':'no-cache',
	'referer':'https://m.yxshiyong.com/',
	'sec-ch-ua':'" noT A;brand";v="99", "chromium";v="90", "googlE chrome";v="90"',
	'sec-ch-ua-mobile':'?0',
	'sec-fetch-dest':'empty',
	'sec-fetch-mode':'cors',
	'sec-fetch-site':'same-site',
	'user-agent':'mozilla/5.0 (windowS NT 6.1; win64; x64) appLewEbkit/537.36 (KHTML, likE gecko) chrome/90.0.4430.93 safari/537.36'}

acc_list=['131','136','1312','132']

whlie acc_list:
    acc=acc_list.pop()
    data['token']=rob_login.login(acc)
    res=requests.post(apiUrl,headers=header,json=data).json()
    
