import random as _1,sys as _2;_3="Hello, World!";_4="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ, !";_5=len(_3)
def _6(s):return sum(s[i] != _3[i] for i in range(_5))
def _7():return ''.join(_1.choice(_4) for _ in range(_5))
def _8(s):i=_1.randint(0,_5-1);return s[:i]+_1.choice(_4)+s[i+1:]
_9=_7();_10=_6(_9)
_11=0
while _10 > 0:
    _12 = _8(_9)
    _13 = _6(_12)
    _11 += 1
    if _13 < _10:
        _10 = _13
        _9 = _12
    if _11 % 1000 == 0:
        print({_9})
        print({_11})
print(f"{_9},{_11}")
