import nest_asyncio
import pandas as pd
import twint
import pickle
from IPython.display import clear_output

with open('Persian_swear_words.txt','r') as l:
    bw=l.read().split(', ')

remove_columns=['id', 'conversation_id', 'created_at', 'date', 'timezone', 'place',
       'language', 'hashtags', 'cashtags', 'user_id', 'user_id_str',
       'username', 'name', 'day', 'hour', 'link', 'urls', 'photos', 'video',
       'thumbnail', 'retweet', 'nlikes', 'nreplies', 'nretweets', 'quote_url',
       'search', 'near', 'geo', 'source', 'user_rt_id', 'user_rt',
       'retweet_id', 'reply_to', 'retweet_date', 'translate', 'trans_src',
       'trans_dest']

def Crawling_insults():

    nest_asyncio.apply()

    #crawling insult samples from twitter

    for i,word in enumerate(bw):
        
        c = twint.Config()

        c.Search = [word]
        c.Pandas = True
        c.Lang = "fa" #does'nt work as expected
        c.Limit = 3000

        twint.run.Search(c)
        df=twint.storage.panda.Tweets_df
        df=df.drop(remove_columns,axis=1)
        df.to_csv(f'mini insult csv files/{i+1}.csv', index=False)
        clear_output()
        print(f'done:{i+1}')
        
    print('Crawling_insults done')