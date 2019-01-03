#! /usr/bin/python3

import sys
import json

for line in sys.stdin:
    try:
        tweet = json.loads(line)
        if 'retweeted_status' in tweet:
            origin_tweet = tweet['retweeted_status']
            print(origin_tweet['retweet_count'], 1, sep=' ')
    except:
        continue
