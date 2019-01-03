#!/usr/bin/python3

import sys
import json

# Hashtags
for line in sys.stdin:
    try:
        tweet = json.loads(line)
        for item in tweet['entities']['hashtags']:
            print(item['text'], 1, sep=' ')
    except:
        continue

