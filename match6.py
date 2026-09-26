import re                        # 导入re模块
# 表达式,h开头，n$表示n结尾
pattern = r'h\w+\s[\u4e00-\u9fa5]+\s\w+n$'
match = re.match(pattern,'hello 我爱 Python')  # 匹配字符串
print(match)                            # 打印匹配结果
print(match.group())                    # 打印所有匹配内容
