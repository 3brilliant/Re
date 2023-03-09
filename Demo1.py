
import re

s = '10086111222'

# 5 - 11 位电话号码

result = re.match(r'[1-9]\d{4,10}$', s)

print(result)