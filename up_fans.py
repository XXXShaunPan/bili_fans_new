import requests as rq
import os
import pandas as pd

df=pd.read_csv('bili_fans/up_fans_new.csv',index_col=[0])
# df=pd.DataFrame(index=['mid'])
cookie=process.env.XZ_COOKIE

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


a={"indexType":0,"field":"","sort":"addFollowerCount","interval":"day","size":60,"start":1}


def proc(da,date):
	for i in da:
	    num=i['addFollowerCount'].replace("-","")
	    if 'w' in num:
	        num=num.replace("w",'')
	        num=eval(num)*10000
	    if i['name'] not in df.columns:
	    	df[i['name']]=[0]*len(df.index)
	    	df[i['name']]['mid']=i['mid']
	    if date not in df.index.tolist():
	   	 	df.loc[date]=[0]*len(df.columns)
	    df[i['name']][date]=int(num)
	    # up_pic(i['face'],i['mid'])
	    print(i['name'])

# def up_pic(url,mid):
# 	if not os.path.exists(f"up_pic/{mid}.jpg"):
# 		pic=rq.get(url,headers=header1).content
# 		with open(f'up_pic/{mid}.jpg','wb') as f:
# 			f.write(pic)



def spider_all_day():
	res=rq.post("https://xz.newrank.cn/nr/bili/rank/singleIndex",json=a,headers=header).json()['data']
	date=res['update_time'].split(" ")[0]
	proc(res['list'],date)

def main():
	spider_all_day()
	df.to_csv('bili_fans/up_fans_new.csv',index=True,header=True)

if __name__ == '__main__':
	main()
