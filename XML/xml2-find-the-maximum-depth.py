"""
https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth
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

1
"""

import xml.etree.ElementTree as etree

def find_depth(root, depth = 0):
    return max(find_depth(x, depth+1) for x in root) if root else depth

no_lines = int(input())
xml_source = '\n'.join(input() for _ in range(no_lines))
tree = etree.ElementTree(etree.fromstring(xml_source))

print(find_depth(tree.getroot()))

