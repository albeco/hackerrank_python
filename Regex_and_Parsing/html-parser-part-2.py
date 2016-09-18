"""
https://www.hackerrank.com/challenges/html-parser-part-2
Language: Python 3

Sample Input

4
<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->

Sample Output

>>> Multi-line Comment
[if IE 9]>IE9-specific content
<![endif]
>>> Data
 Welcome to HackerRank
>>> Single-line Comment
[if IE 9]>IE9-specific content<![endif]
"""

from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data.strip():
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        print(data)
    def handle_data(self, data):
        if data.strip():
            print('>>> Data')
            print(data)

no_lines = int(input())
html_source = '\n'.join(input() for _ in range(no_lines))

parser = MyHTMLParser()
parser.feed(html_source)
parser.close()
