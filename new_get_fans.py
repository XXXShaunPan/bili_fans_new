import pandas as pd
from random import shuffle
import os
import main_color


type="up" if os.environ["fans_type"] else "down"
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
# 	 a	b
# 0	 5	2               a    18
# 1	 4	5	 --->		b     8
# 2	 9	1				

dict_data={'cname':df1.index,'近期掉粉总榜':df1.values}
dict_data=pd.DataFrame(dict_data)

df1=pd.DataFrame(dict_data.T,index=dict_data.columns,columns=dict_data.index)
df1.columns=a
df1.loc['desc']=['']*len(df.columns)
b=df1.loc['近期掉粉总榜'].tolist()
shuffle(b)
df1.loc['近期掉粉总榜_开头']=b
df1.loc['color']=main_color.main(a)
df1=df1.reindex(index=['cname','color','desc','近期掉粉总榜_开头','近期掉粉总榜'])
df1.to_csv(f'bili_UP_pic/{type}.csv',header=True,index=True)

