import re                        # 导入re模块
pattern = r'hello|我'                 # 表达式,表示需要匹配“hello”或“我”开头的字符串
match = re.match(pattern,'hello word')  # 匹配字符串
print(match)                            # 打印匹配结果
match = re.match(pattern,'我爱Python')  # 匹配字符串
print(match)