import pandas as pd
from random import shuffle
import os

type="up" if os.environ["get_fans_type"] else "down"
df1=pd.read_csv(f'bili_fans/{type}_fans_new.csv',index_col=[0])

m,d=os.environ["date_start"].split('-')

df=df1.loc['2021-'+m+'-'+d:]
df.loc['mid']=[0]*len(df.columns)

for i in df.columns:
	if df[i].tolist()==[0]*len(df.index):
		print(i)
		del(df[i])
	else:
		df.loc['mid'][i]=df1.loc['mid'][i]

a=df.loc['mid'].tolist()
df1=df.drop(["mid"]).apply(lambda x: x.sum(),axis=0)
dict_data={'cname':df1.index,'总榜':df1.values}
dict_data=pd.DataFrame(dict_data)
df1=pd.DataFrame(dict_data.T,index=dict_data.columns,columns=dict_data.index)
df1.columns=a
df1.loc['desc']=['']*len(df.columns)
b=df1.loc['总榜'].tolist()
shuffle(b)
df1.loc['近期掉粉总榜']=b
df1.to_csv(f'bili_fans/{type}.csv',header=True,index=True)
# print('\n\n\n\n\n\n'+df.loc['mid'])
