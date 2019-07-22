#!/usr/bin/env python3
import requests
import re
from sympy.solvers import solve, solveset
from sympy import Symbol, Eq
#from string import whitespace
 
url = 'http://cbweb.cyberbattle.info:8008/index.php?name=ctf2019'
s = requests.Session()
r = s.get(url)
print(r.text)
 
flag=[]
counter = 1
while (1):
    m = re.findall(r'<pre>(.*)</pre', r.text)[0]
    answer = eval(m)
    print(answer)
    r = s.get(url + "&math=" + str(answer))
    counter = counter+1
    print(counter, r.text)
    if(re.findall(r'Congrats', r.text)):
       flag.append(re.findall(r'<b>(.*)</b>', r.text))
       print(flag)