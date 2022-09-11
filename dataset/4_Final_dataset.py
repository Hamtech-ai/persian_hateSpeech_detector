import pandas as pd

df1=pd.read_csv('chats.csv')
df2=pd.read_csv('insults.csv')

df=pd.concat([df1,df2],ignore_index=True)
df = df.sample(frac = 1,ignore_index=True)
df.to_csv('data.csv', index=False)