import pandas as pd

def Final_dataset():

    df1=pd.read_csv('chats.csv')
    df2=pd.read_csv('insults.csv')

    df=pd.concat([df1,df2],ignore_index=True)
    df=df.drop(df[df['text'].str.len()<2].index)
    df = df.sample(frac = 1,ignore_index=True)
    df.to_csv('data.csv', index=False)
    
    print('Final_dataset done')