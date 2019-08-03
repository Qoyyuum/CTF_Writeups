#!/usr/bin/env python3
import requests
import re

url = 'http://hitemup.cb.ctf:8181'
s = requests.Session()
r = s.get(url)
# print(r.text)
found = True
while (found):
    flag = re.findall(r"<h1>(.*)<\/h1>", r.text)[0]
    header = re.findall(r"<h1> (.*)<\/h1>", r.text)[0]
    first = re.findall(r"<h1> \.egap siht fo rotisiv ht([0-9])[0-9][0-9].*<\/h1>", r.text)[0]
    second = re.findall(r"<h1> \.egap siht fo rotisiv ht[0-9]([0-9])[0-9].*<\/h1>", r.text)[0]
    third = re.findall(r"<h1> \.egap siht fo rotisiv ht[0-9][0-9]([0-9]).*<\/h1>", r.text)[0]


    print(header)
    print("Flag: ", flag)
    print(first, second, third)
    print(r.text)
    r = s.get(url)

    if first == 0:
        if second == 0:
            if third == 5:
                print("Found 005!")
                print(r.text)
                print("Found 005!")
                print("Found 005!")
                print("Found 005!")
                found = False
    else:
        r = s.get(url)

# }sihTdetpircSuoYepoHi{FTCBC
# CBCTF{iHopeYouScriptedThis}