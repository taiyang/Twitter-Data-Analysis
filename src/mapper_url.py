#! /usr/bin/python3

import sys
import json

for line in sys.stdin:
    try:
        tweet = json.loads(line)
        for item in tweet['entities']['urls']:
            print(item['url'], item['expanded_url'], 1, sep=' ')
    except:
        continue
