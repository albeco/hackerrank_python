"""
https://www.hackerrank.com/challenges/hex-color-code
Language: Python 3

Sample Input

11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}   

Sample Output

#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff
"""

import re

no_lines = int(input())
text_lines = []
for _ in range(no_lines):
    text_lines.append(input().strip())
text = ' '.join(text_lines)

get_color = re.compile(r'#(?:[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]){1,2}')
colors = []
for tag in re.findall(r'{.*?}',text):
    colors.extend(get_color.findall(tag))
    
print(*colors, sep='\n')
