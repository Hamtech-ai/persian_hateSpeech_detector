import pandas as pd
import numpy as np
import os
from langdetect import detect

def Insults_dataset():

    csv_lists=[csv for csv in os.listdir('mini insult csv files/') if '.csv' in csv]
    df=pd.DataFrame()

    for i in csv_lists:
        csv=pd.read_csv(f'mini insult csv files/{i}', engine='python')
        df=pd.concat([df,csv])
        
    df['tweet']=df['tweet'].str.replace('[^۰۹۸۷۶۵۴۳۲۱الفبپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی ]','')
    df=df.drop_duplicates(keep='first')
    df=df.dropna()
    df.index=range(len(df))
    df=df.drop(df[df['tweet'].str.contains('[الفبپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی]')==False].index)
    df.index=range(len(df))

    for i,t in df['tweet'].items():
        if detect(t)=='ar':
            df=df.drop(i)
        else:continue

    df['label']=np.ones(len(df),dtype="int")
    df.columns=['text','label']
    df.to_csv('insults.csv', index=False)
    
    print('Insults_dataset done')