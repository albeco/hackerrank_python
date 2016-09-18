"""
https://www.hackerrank.com/challenges/decorators-2-name-directory
Language: Python 3

Sample Input

3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F

Sample Output

Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle
"""

def sorted_names_list(f):
    def func(s):
        name_list = [entry.split() for entry in s]
        sorted_list = sorted(name_list, key = lambda x: int(x[2]))    
        return f(sorted_list)
    return func

@sorted_names_list
def print_directory(name_list):
    for name in name_list:
        title = 'Mr. ' if name[-1]=='M' else 'Ms. '
        print(title + ' '.join(name[0:2]))

n = int(input())
s = [input() for _ in range(n)]
print_directory(s)
