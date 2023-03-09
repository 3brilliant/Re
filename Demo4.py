import re

# 用户名只能包含数字、字母、下划线，不能以数字开头，长度在6到16位范围内

s = 'xzq_2234w'

result = re.match('^[a-z_][a-z\d_]{5,15}$', s)

print(result)