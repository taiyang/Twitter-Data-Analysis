#!/usr/bin/python3

import sys


total = 0
old_key = None
old_key2 = None
for line in sys.stdin:
    if len(line.split()) != 3:
        continue
    key, key2, value = line.split()
    if old_key and key != old_key:
        print(old_key, old_key2, total, sep=' ')
        total = 0

    old_key = key
    old_key2 = key2
    total += int(value)

if old_key is not None:
    print(old_key, old_key2, total, sep=' ')
