#Adding Up

Question:
I love adding up previous two numbers. 
def ct(f):
return f if f < 2 else ct(f-2) + ct(f-1) 

print "Your flag is:" + str(ct(2019))[:42]

Answer:
I didn't understand the question. I can see its a simple of adding two numbers (previous 2 numbers?). Anyways, didn't get the flag but someone did. Fitri shared his little code that sort of made sense to me. To get the flag, run the `getflag.py` script and the last result is the flag. `CBCTF{639069811559435586651349273985287139381962}`
