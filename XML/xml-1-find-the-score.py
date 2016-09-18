"""
https://www.hackerrank.com/challenges/xml-1-find-the-score
Language: Python 3

Sample Input

6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>

Sample Output

5
"""

import xml.etree.ElementTree as etree

no_lines = int(input())
xml_source = '\n'.join(input() for _ in range(no_lines))
tree = etree.ElementTree(etree.fromstring(xml_source))
print(sum(len(x.attrib) for x in tree.iter()))
