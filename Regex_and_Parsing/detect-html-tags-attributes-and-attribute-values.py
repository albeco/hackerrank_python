"""
https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values
Language: Python 3

Sample Input

9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>

Sample Output

head
title
object
-> type > application/x-flash
-> data > your-file.swf
-> width > 0
-> height > 0
param
-> name > quality
-> value > high
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
        continue
    print(tag.groupdict()['argument'])
    if tag.groupdict()['attributes']:
        attr_list = get_attr.finditer(tag.groupdict()['attributes'])
        for at in attr_list:
            print('-> {key} > {value}'.format(**at.groupdict()))

