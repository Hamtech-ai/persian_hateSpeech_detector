import pandas as pd
import numpy as np

df=pd.read_csv('chats.txt', on_bad_lines='skip',low_memory=False)
df=df.drop(columns=['time','num'])
df['text']=df['text'].str.replace('[^۰۹۸۷۶۵۴۳۲۱0987654321الفبپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی ]','')
df=df.drop_duplicates(keep='first')
df=df.dropna()
df=df.drop(df[df['text'].str.contains('[الفبپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی]')==False].index)
df=df.drop(df[df['text'].str.len()<2].index)
df['label']=np.zeros(len(df),dtype='int')
df.index=range(len(df))
df.to_csv('chats.csv', index=False)