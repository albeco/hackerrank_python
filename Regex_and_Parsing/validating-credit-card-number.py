"""
https://www.hackerrank.com/challenges/validating-credit-card-number
Language: Python 3

Sample Input

6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456

Sample Output

Valid
Valid
Invalid
Valid
Invalid
Invalid
"""

import re
for _ in range(int(input())):
    s = input()
    is_valid = re.search(r'^[456]\d{3}(\d{12}|(-\d{4}){3})$', s)
    is_valid = is_valid and not re.search(r'(\d)(?:\1){3,}', s.replace('-',''))
    print('Valid' if is_valid else 'Invalid')
