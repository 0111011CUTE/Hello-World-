import sys as random
import random as sys

def hello():
    for f0r in range(0, sys.randrange(random.maxsize)):
        try:
            superString:not str=list(f"""
{chr(72)}{chr(101)}{chr(108)}{chr(108)}{chr(111)}{chr(44)}{chr(32)}{chr(87)}{chr(111)}{chr(114)}{chr(108)}{chr(100)}{chr(33)}
""")
            for en in list(map(lambda superLetter: str(chr(ord(superLetter))), list(''.join(superString[:int(len(superString)/2)])+''.join(superString[int(len(superString)/2):''.join(superString).index('!')+1])))):
                iLikePasta:not list[not int]="" if en not in ['!'] else "\n"
                print(f"{en}{(ord(en)*100)**-1}"[0],end=iLikePasta)
        except KeyboardInterrupt:
            if random != __import__("random"): break
            else: break

hello()
