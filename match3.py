import re                        # 导入re模块
pattern = '.ello'                 # 表达式
match = re.match(pattern,'hello')  # 匹配字符串
print(match)                      # 打印匹配结果
match = re.match(pattern,'aello')  # 匹配字符串
print(match)
match = re.match(pattern,'6ello')  # 匹配字符串
print(match)
