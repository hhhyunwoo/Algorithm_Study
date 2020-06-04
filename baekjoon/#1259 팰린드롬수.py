#1259 팰린드롬수

import sys
import operator
input=sys.stdin.readline

if __name__ == "__main__":
   while 1:
      val = str(input().rstrip())
      val_in=val[::-1]
      if val=='0':break
      if val==val_in:
         print('yes')
      else:
         print('no')