
import re

# 座机号码
phone = '010-12345678'

result = re.match(r'(\d{3}|\d{4})-(\d{8})$', phone)

print(result)

