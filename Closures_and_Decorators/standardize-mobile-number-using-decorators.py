"""
https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators
Language: Python 3

Sample Input

3
07895462130
919875641230
9195969878

Sample Output

+91 78954 62130
+91 91959 69878
+91 98756 41230
"""

import re
def format_nums(f):
    def func(num):
        fmt_nums = [re.sub(r'(\+?91|0)?(\d{5})(\d{5})', r'+91 \2 \3', x) for x in num]
        return f(fmt_nums)
    return func

@format_nums
def print_nums(s):
    print(*sorted(s), sep='\n')

n = int(input())
num_list = [input() for _ in range(n)]
    
print_nums(num_list)
