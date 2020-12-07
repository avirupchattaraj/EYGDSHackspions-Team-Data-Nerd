import glob,os
from pathlib import Path
base = Path(__file__).resolve().parent.parent.parent
os.chdir(base)
#os.chdir(r"EYSociolytics/")
lst=glob.glob("*.csv")
last_file=lst[-1]
#print(lst)


import numpy as np
import pandas as pd
import spacy
import sklearn
import matplotlib.pyplot as plt
from textblob import TextBlob
import re
import preprocessor as p
from wordcloud import WordCloud
import seaborn as sns
import json
import nltk
nltk.download('stopwords')
import string
from nltk.corpus import stopwords
stopWords = set(stopwords.words('english'))
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

path=str(base)+"\\"+last_file





def sentiment_average_calculator():
    data=pd.read_csv(path)
    data.drop(['near','geo','source','user_rt_id','user_rt','retweet_id','retweet_date','translate','trans_src','trans_dest'],axis=1,inplace=True)
    data.drop("reply_to",axis=1,inplace=True)
    data.drop("cashtags",axis=1,inplace=True)
    data.drop("place",axis=1,inplace=True)
    data.drop(['id','conversation_id','created_at','date'],axis=1,inplace=True)
    data.drop(['time','timezone','user_id'],axis=1,inplace=True)
    data.drop(['username','name'],axis=1,inplace=True)
    data['splitted_message']=data['tweet'].apply(lambda message:str(message).split())
    def hashtag_finder(message):
        tweet = re.findall(r'#[a-zA-Z]+',str(message))
        hashtags=""
        for i in tweet:
            hashtags+=i
            hashtags+=" "
        return hashtags
    data['hashtag']=data['splitted_message'].apply(hashtag_finder)

    def clean_message(lst):
        message=''
        for i in lst:
            if str(i) in stopWords:
                continue
            elif str(i) in string.punctuation:
                continue
            elif str(i) in string.digits:
                continue
            else:
                message+=str(i)
                message+=" "
        return message
    
    data['semi_clean']=data['splitted_message'].apply(clean_message)
    def clean_text(message):
        clean_message=p.clean(message)
        return clean_message


    data['cleaned_message']=data['semi_clean'].apply(clean_text)

    def sentiment_calculator(message):
        cleaned_message=p.clean(message)
        blob=TextBlob(message)
        return blob.sentiment.polarity
    
    data['polarity_score']=data['cleaned_message'].apply(sentiment_calculator)

    def vader_sentiment_calculator(message):
        score1 = analyser.polarity_scores(message)
        return score1.get('compound')
        
    data["vader_sentiment_score"]=data['cleaned_message'].apply(vader_sentiment_calculator)

    def sentiment_category(score):
        if score >= 0.05:
            return "Positive"
        elif score > -0.05 and score <0.05:
            return "Neutral"
        elif score <= -0.05 : 
            return "Negative"
            
    data['sentiment_category']=data['vader_sentiment_score'].apply(sentiment_category)
    
    data_platform=dict(data['sentiment_category'].value_counts())
    for key in data_platform:
        data_platform[key]=data_platform[key]/len(data)

    #print(data_platform)
    print(path)

    return json.dumps(data_platform)



def hashtags_finder():
    data=pd.read_csv(path)
    data['splitted_message']=data['tweet'].apply(lambda message:str(message).split())
    def hashtag_finder(message):
        tweet = re.findall(r'#[a-zA-Z]+',str(message))
        hashtags=""
        for i in tweet:
            hashtags+=i
            hashtags+=" "
        return hashtags
    data['hashtag']=data['splitted_message'].apply(hashtag_finder)

    hashtags=""
    for i in data['hashtag']:
        dat=i.split("#")
        for j in dat:
            if dat!="":
                hashtags+=j
                hashtags+=" "

    return hashtags

    
    
    















