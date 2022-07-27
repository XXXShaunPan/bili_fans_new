#coding=utf-8
import requests as rq
import time


appid="wxb54c35a43b3bab1d"
secret="bf021753109e9a31b2e1c4373425474f"

url_get_token=f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={secret}"
url=lambda access_token:f"https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={access_token}"
# http://pushplus.hxtrip.com/send?token=5a29cd5885644333ac530e02060a15de&title=XXX&content=XXX&template=html

def sendMessage(desp,link="https://pioooo.ml"):
    data={
        "token":"5a29cd5885644333ac530e02060a15de",
        "title":desp,
        "content":link
    }
    rq.post(f"http://pushplus.hxtrip.com/send",headers={'content-type':'application/json;charseT=UTF-8'},json=data)


def sendMessage_old(desp,link="https://pioooo.ml"):
    try:
        with open('token.txt','r') as f:
            token=f.read()
    except:
        token='12312312'
    # print(token)
    data={

        "touser":"ocAHF6CgexoGG6xLEalDJuEBFNEk",

        "template_id":"4ORaT-FOFzhDae1Qsm29dZSDDlQKmkK24XtCU7x8FO0",

        "url":link,

        "topcolor":"#FF0000",

        "data":{
                "title": {
                    "value":"抢单通知\n\n\n",
                    "color":"#ff3399"
                },
                "content":{
                    "value":desp,

                    "color":"#0099CC"
                },
                "time_now":{

                    "value":"\n\n\t\t\t\t\t\t\t当前时间：" + time.strftime("%m-%d:%H:%M:%S",time.localtime()),

                    "color":"#030303"
                }
          }
    }
    i=2
    while i:
        res=rq.post(url(token),json=data).json()
        i-=1
        if res['errcode']:
            print('获取新的')
            token=rq.get(url_get_token).json()['access_token']
            with open('token.txt','w') as f:
                f.write(token)
        else:
            break
    return res

if __name__ =="__main__":
	print(sendMessage_old("发送","https://item.taobao.com/item.htm?spm=a21dvs.23580594.0.0.47b33d0dEpLOGL&ft=t&id=668695450774"))
