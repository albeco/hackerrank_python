"""
https://www.hackerrank.com/challenges/html-parser-part-1
Language: Python 3

Sample Input

2
<html><head><title>HTML Parser - I</title></head>
<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>

Sample Output

Start : html
Start : head
Start : title
End   : title
End   : head
Start : body
-> data-modal-target > None
-> class > 1
Start : h1
End   : h1
Empty : br
End   : body
End   : html
"""

import re

no_lines = int(input())
html_source = ''
for _ in range(no_lines):
    html_source += input()

find_comments = re.compile('<!--[\S\s]*?-->')
html_source = find_comments.sub('', html_source)

find_tags = re.compile(r'<(?P<start_slash>/?)\s*(?P<argument>\w+)\s*(?P<attributes>[\s\S]*?)\s*(?P<end_slash>/?)>')
get_attr = re.compile(r'(?P<key>[\w-]+)\s*(?:=\s*[\"\'](?P<value>[\s\S]+?)[\"\'])?')

for tag in find_tags.finditer(html_source):
    if tag.groupdict()['start_slash']:
        prompt = 'End'
    elif tag.groupdict()['end_slash']:
        prompt = 'Empty'
    else:
        prompt= 'Start'
    print('{0:5s} : {1:}'.format(prompt, tag.groupdict()['argument']))
    if tag.groupdict()['attributes']:
        attr_list = get_attr.finditer(tag.groupdict()['attributes'])
        for at in attr_list:
            print('-> {key} > {value}'.format(**at.groupdict()))
