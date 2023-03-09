import re
from functools import reduce

# 提取数字并计算
s = '-3.14good87nice19bye'

nums = re.findall(r'-?\d+\.?\d*', s)

result = reduce(lambda x, item: x + float(item), nums, 0)

print(result)