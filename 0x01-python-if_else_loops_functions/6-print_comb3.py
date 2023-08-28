#!/usr/bin/python3
for a in range(10):
    for b in range(a + 1, 10):
        if a == 0:
            print(f"{b:02d}, ", end='')
        elif a == 8 and b == 9:
            print(f"{a:01d}{b:01d}")
        else:
            print(f"{a:01d}{b:01d}, ", end='')
print()
