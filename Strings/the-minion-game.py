"""
https://www.hackerrank.com/challenges/the-minion-game
language: Python 3

Sample Input

BANANA

Sample Output

Stuart 12
"""

s = input()

score1 = score2 = 0
vowels = ['A','E','I','O','U']
for i in range(len(s)):
    if s[i] in vowels:
        score1 += len(s)-i
    else:
        score2 += len(s)-i

if score1==score2:
    print('Draw')
elif score1>score2:
    print('Kevin',score1)
else:
    print('Stuart',score2)