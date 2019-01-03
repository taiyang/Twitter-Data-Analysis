#!/usr/bin/python3

import sys


total = 0
old_key = None
for line in sys.stdin:
    if len(line.split()) != 2:
        continue
    key, value = line.split()
    if old_key and key != old_key:
        print(old_key, total, sep=' ')
        total = 0

    old_key = key
    total += int(value)

if old_key is not None:
    print(old_key, total, sep=' ')
