#!/usr/bin/env python3
def countme():
    a = [1,1]
    for x in range(2,2020):
        x = a[-1] + a[-2]
        a.append(x)
        print str(x)[:42]

countme()
