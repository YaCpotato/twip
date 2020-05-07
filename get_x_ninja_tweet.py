# -*- coding:utf-8 -*-
import json, config
from requests_oauthlib import OAuth1Session
import csv

def searchWordsRecurrent(from_date, to_date,res = None):
    url = "https://api.twitter.com/1.1/tweets/search/fullarchive/MyPortfolio.json"
    keyword = "Ma_gician"
    print('----------------------------------------------------')
    params = {'query' : keyword, 'maxResults' : 100,'fromDate':from_date,'toDate':to_date}

    #レスポンスが引数で与えられていたら
    if res is not None:
        params['next'] = res['next']
    result = twitter.get(url, params = params)

    #CSVのヘッダーを定義
    header = ['id','User Name','User ID','Follows','Followers','User Location','content','time']
    search_timeline = {}
    if result.status_code == 200:
         with open('data/{keyword}from{from_date}_to{to_date}.csv'.format(keyword = keyword, from_date = from_date, to_date = to_date), 'w') as f:
             search_timeline = json.loads(result.text)
             writer = csv.writer(f)
             writer.writerow(header)
             for tweet in search_timeline['results']:
                 tmp = []
                 tmp.append(tweet['id'])
                 tmp.append(tweet['user']['name'])
                 tmp.append(tweet['user']['screen_name'])
                 tmp.append(tweet['user']['friends_count'])
                 tmp.append(tweet['user']['followers_count'])
                 tmp.append(tweet['user']['location'])
                 tmp.append(tweet['text'])
                 tmp.append(tweet['created_at'])
                 writer.writerow(tmp)
                 tmp = []
             print(len(search_timeline['results']))
    else:
        print("ERROR: %d" % req.status_code)
    if 'next' in search_timeline:
        searchWordsRecurrent(from_date, to_date,search_timeline)

    return;

if __name__ == '__main__':
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET
    twitter = OAuth1Session(CK, CS, AT, ATS)
    searchWordsRecurrent("201906010000", "201907010000")
