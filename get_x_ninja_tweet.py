# -*- coding:utf-8 -*-
import json, config
from requests_oauthlib import OAuth1Session
import csv


def searchWords(from_date, to_date):
    url = "https://api.twitter.com/1.1/tweets/search/fullarchive/MyPortfolio.json"
    keyword = "Ma_gician"
    print('----------------------------------------------------')
    params = {'query' : keyword, 'maxResults' : 100,'fromDate':from_date,'toDate':to_date}
    req = twitter.get(url, params = params)
    header = ['id','User Name','User ID','Follows','Followers','User Location','content','time']
    if req.status_code == 200:
        with open('data/{keyword}from{from_date}_to{to_date}.csv'.format(keyword = keyword, from_date = from_date, to_date = to_date), 'w') as f:
            search_timeline = json.loads(req.text)
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
            return;
    else:
        print("ERROR: %d" % req.status_code)
    return;

if __name__ == '__main__':
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET
    twitter = OAuth1Session(CK, CS, AT, ATS)
    searchWords("201908010000", "201908100000")
