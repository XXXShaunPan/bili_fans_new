import requests as rq
import os,random
import pandas as pd
import send_mail

df=pd.read_csv('bili_fans/down_fans_new.csv',index_col=[0])
# df=pd.DataFrame(index=['mid'])
cookie=os.environ["XZ_COOKIE"]

header={"Host": "xz.newrank.cn"
	 ,"Connection": "keep-alive"
	 ,"Content-Length": "90"
	 ,"Accept": "application/json, text/plain, */*"
	 ,"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/,87.0.4280.88 Safari/537.36"
	 ,"Content-Type": "application/json;charset=UTF-8"
	 ,"Origin": "https://xz.newrank.cn"
	 ,"Sec-Fetch-Site": "same-origin"
	 ,"Sec-Fetch-Mode": "cors"
	 ,"Sec-Fetch-Dest": "empty"
	 ,"Accept-Encoding": "gzip, deflate, br"
	 ,"Accept-Language": "zh-CN,zh;q=0.9"
	 ,"Cookie": cookie
 }


a={"indexType":6,"field":"","sort":"addFollowerCount","interval":"day","size":50,"start":1}


def proc(da,date):
	out=''
	for i in da:
	    num=i['addFollowerCount'].replace("-","")
	    if 'w' in num:
	        num=num.replace("w",'')
	        num=eval(num)*10000+random.randint(1,100)
	    if i['name'] not in df.columns:
	    	df[i['name']]=[0]*len(df.index)
	    	df[i['name']]['mid']=i['mid']
	    if date not in df.index.tolist():
	   	 	df.loc[date]=[0]*len(df.columns)
	    df[i['name']][date]=int(num)
	    # down_pic(i['face'],i['mid'])
	    out+=f"{i['name']}=={int(num)}\n"
	send_mail.run(title='掉粉情况推送',content=out)

# def down_pic(url,mid):
# 	if not os.path.exists(f"down_pic/{mid}.jpg"):
# 		pic=rq.get(url,headers=header1).content
# 		with open(f'down_pic/{mid}.jpg','wb') as f:
# 			f.write(pic)



def spider_all_day():
	res=rq.post("https://xz.newrank.cn/nr/bili/rank/singleIndex",json=a,headers=header).json()['data']
	date=res['update_time'].split(" ")[0]
	proc(res['list'],date)
	#print(res)

def main():
	spider_all_day()
	df.to_csv('bili_fans/down_fans_new.csv',index=True,header=True)

if __name__ == '__main__':
	main()
