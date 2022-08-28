#coding=utf-8
import requests
import time,sys
from datetime import datetime
import rob_login,wx_message
# from pytz import timezone

is_force=True
if sys.argv[-1] == '1':
	is_force=True
	sys.argv.pop()

if len(sys.argv)>4:
    time.sleep(int(sys.argv[4])*60)

#          1：商品   2：账号  3：买号
# 商品号
yongid=sys.argv[1]
# 登录账号
login_acc=sys.argv[2] if len(sys.argv)>2 else '136'

# 	   13650878173
# 108588, "tb202106299"
# 106720, "tb630077372"
# 105598, "无贤静夜"
# 104189, "tb406187828"
# 100508, "tb406187829"

# 	    13119548020
#   95507, "tb264447547"
#   95531, "小shaunpan"
#   97407, "t_1510240925627_04..."
#   106718, "小小shaun"
#   108045, "tb6300773723"

# 	    13246485632
# 126317,"tb2754472458", flagname: "已通过"}
# 111113 "tb2000102801", num_month: 21, num_week: 2}
# 111682 "tb460113775", num_month: 3, num_week: 1}
# 112721 "tb3637883813", num_month: 21, num_week: 2}
# 115002 "小shaunpan.", num_month: 8, num_week: 1}

#       13128268173   
#0: {bindid: 120483, webid: 1, bindname: "tb991207421", flag: 2, webname: "淘宝天猫", flagname: "已通过"}
#1: {bindid: 119422, webid: 1, bindname: ".小shaunpan", flag: 2, webname: "淘宝天猫", flagname: "已通过"}
#2: {bindid: 113925, webid: 1, bindname: "tb6300773721", flag: 2, webname: "淘宝天猫", flagname: "已通过"}
#3: {bindid: 111610, webid: 1, bindname: "tb33133306", flag: 2, webname: "淘宝天猫", flagname: "已通过"}


ids={
	'136':[108588,106720,105598,104189,100508],
	'132':[111682,115002,111113,126317,112721],
	'131':[95507,95531,97407,106718,108045],
	'1312':[120483,119422,113925,111610,129393]
}

apiUrl="https://apim.yxshiyong.com/home/Yongshow/apply"
timeUrl='https://apim.yxshiyong.com/home/Yongshow/details'
data={"yongid":yongid,"bindid":123,"is_storename":"","token":123}

data['bindid']=sys.argv[3] if len(sys.argv)>3 else ids[login_acc].pop()

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

res=requests.post(timeUrl,headers=header,json=data).json()
nexttime=res['data']['nexttime']
link=res['data']['pai_linkurl']
print('next:',time.strftime("%m-%d:%H:%M:%S",time.localtime(nexttime)))
print(time.time())
if nexttime-time.time()>5:
	print('沉睡',nexttime-time.time()-5)
	time.sleep(nexttime-int(time.time()-5)
data['token']=rob_login.login(login_acc)
while 1:
	res=requests.post(apiUrl,headers=header,json=data).json()
	# time.sleep(0.4)
	print(res['msg'],time.strftime("%m-%d:%H:%M:%S",time.localtime()))
	if  not is_force and '该买号' in res['msg'] and ids[login_acc]:
		data['bindid']=ids[login_acc].pop()
	# print(time.time())
	elif '审核' in res['msg']:
		# print(res['msg'])
		wx_message.sendMessage_old(f'{yongid}--{login_acc}--{data["bindid"]}--抢成功了',link)
		break
	elif nexttime<time.time()-3 or not ids[login_acc]:
		wx_message.sendMessage_old(f'{yongid}--没抢到 或 没号={len(ids[login_acc])}')
		break
	elif "请等待放单" in res["msg"]:
		continue
	else:
		wx_message.sendMessage_old(f'{yongid}--{res["msg"]}')
		break
