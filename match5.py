import re                        # 导入re模块
# 表达式，“hello”开头，“\s”中间空格，“（\w+）”分组后面所有字母、数字以及下划线数据
pattern = r'hello\s(\w+)'
match = re.match(pattern,'hello word')  # 匹配字符串
print(match)                            # 打印匹配结果
print(match.group())                    # 打印所有匹配内容
print(match.group(1))                   # 打印分组指定内容