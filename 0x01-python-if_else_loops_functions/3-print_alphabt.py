#!/usr/bin/python3
for c in map(chr, range(ord('a'), ord('z') + 1)):
    if c not in ['q', 'e']:
        print(c, end='')
