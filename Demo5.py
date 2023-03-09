# 爬虫

import re

s = '<html>hello</h1>'

s2 = '<html>hello</html>'

result = re.match(r'<([0-9A-z]+)>(.+)</\1>$', s)

print(result)

result = re.match(r'<([0-9A-z]+)>(.+)</\1>$', s2)

print(result)