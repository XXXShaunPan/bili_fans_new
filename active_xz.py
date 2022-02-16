#coding=utf-8
import requests
import time,sys,os

find_all_api='https://xz.newrank.cn/nr/bili/login/saveAndLogin'

header={"accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/json;charset=UTF-8",
    "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"97\", \"Chromium\";v=\"97\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "cookie": "Hm_lvt_5c88d1bb9ac529f1f4a8b2be9e785fcb=1635565961; Hm_lvt_ab2358e695ccada3424acb6402afd2cb=1635565961; _uab_collina=163556596203126977899184; token=96182B07B95C469086C2C285157C91B2; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22nr_02e52a051%22%2C%22first_id%22%3A%2217e18d0a9621b4-0040f73889a8356-5d11351e-1047552-17e18d0a963762%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217e18d0a9621b4-0040f73889a8356-5d11351e-1047552-17e18d0a963762%22%7D"
}
a={"source":"22","fromUrl":"","unit":"","keyword":""}
res=requests.post(find_all_api,headers=header,json=a).json()

print(res)
