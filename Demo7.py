
import re

#整数或者小数
s = '-3.14'

result = re.fullmatch(r'[+-]?(0|[1-9]\d*)(\.\d+)?', s)

print(result)
