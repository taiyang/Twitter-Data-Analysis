#! /usr/bin/python3

import sys
import json
import string


for line in sys.stdin:
    try:
        tweet = json.loads(line)
        if 'lang' in tweet and tweet['lang'] in ('zh', 'ko', 'ja'):
            for word in tweet['text']:
                print(word, 1, sep=' ')
        else:
            for word in tweet['text'].split():
                print(word.strip(string.punctuation), 1, sep=' ') 
    except:
        continue
