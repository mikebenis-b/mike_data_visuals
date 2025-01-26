import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
pd.options.display.max_columns=None
df=pd.read_csv('data.csv')
df.replace({'H':'HOME','A':'AWAY'},inplace=True)
print(df.head())
print(df.info())

df.loc[(df['Playing_Position'].isna()) & (df['Club']=='Manchester United'),'Playing_Position']='RW'
df.loc[(df['Playing_Position'].isna()) & (df['Club']=='Real Madrid'),'Playing_Position']='LW'
df.loc[(df['Playing_Position'].isna()) & (df['Club']=='Sporting CP'),'Playing_Position']='RW'
print(df.isnull().sum())

print(df.loc[(df['Playing_Position'].isnull())])
shot=['Right-footed shot','Left-footed shot']
df.loc[(df['Type'].isnull()),'Type']=np.random.choice(shot)
print(df.isnull().sum())
print(df.describe())
print(df['Playing_Position'].unique())
print(df['Season'].sort_values().unique())
print(df.Club.unique())
print(df.columns)
nw_df=df.groupby(['Playing_Position','Club']).count()
nw_df=pd.DataFrame(nw_df['Season'])
print(nw_df.columns)
nw_df.columns=['goals']
print(nw_df)
df1=pd.DataFrame(df.Goal_assist.value_counts())[:10]
df1.reset_index(inplace=True)
df1.columns=['players','assist']
print(type(df1['assist']))
print(df1)
plt.figure()
sns.barplot(df1['assist'])
# plt.show()
ranks=[]
for i in range(10):
    ranks.append(f'Rank{i+1}')
print(ranks)
li=pd.to_numeric(df['Minute'],errors='coerce')
# li=pd.cut(df['Minute'],bins=[0,10,20,30,40,50,60,70,80,90,120],labels=['1','2','3','4','5','6','7','8','9','10'])
print(type(li))
df.info()
li.info()
print(li.isnull().sum())
nw=df['Minute'].apply(eval)
print(type(nw))
print(nw)
df['Minute']=nw
lu=pd.cut(df['Minute'],bins=[0,10,20,30,40,50,60,70,80,90,120],labels=['1','2','3','4','5','6','7','8','9','10'])
print(lu.unique)
dc=pd.DataFrame(df['Opponent'].value_counts()[-10:])
dc.reset_index(inplace=True)
dc.columns=['opponents','goals']
print(dc)
print(len(df.At_score.unique()))
print(df.At_score.value_counts()[:10])
dc=pd.DataFrame(df.At_score.value_counts()[:10])
dc.reset_index(inplace=True)
dc.columns=['score_stamp','counts']
print(dc.columns)
