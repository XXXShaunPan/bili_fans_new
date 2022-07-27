import requests

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

def login(acc):
    acc=[i for i in ['13119548020','13650878173','13246485632','13128268173'] if acc in i][0]
    data={"username": acc, "password": "a630077372", "token":""}
    res=requests.post("https://apim.yxshiyong.com/home/loginreg/Login",headers=header,json=data).json()
    return res['data']['token']
