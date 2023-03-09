
import re

s = '1.py 2.png ssx.csv qaq.txt xzq.py'

# 文件名格式: (数字字母_).py

result = re.findall(r'\w+\.py\b', s)

print(result)