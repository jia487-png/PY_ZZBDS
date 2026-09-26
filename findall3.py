import re                        # 导入re模块
pattern = 'https://.*(\d+).com/'               # 表达式，“.*”获取www.hao123.com
match = re.findall(pattern,'https://www.hao123.com/')  # 匹配字符串
print(match)                            # 打印匹配结果



pattern = 'https://.*?(\d+).com/'               # 表达式，“.*”获取www.hao123.com
match = re.findall(pattern,'https://www.hao123.com/')  # 匹配字符串
print(match)                            # 打印匹配结果



pattern = 'https://(.*?)'               # 表达式，“.*?”获取www.hao123.com/
match = re.findall(pattern,'https://www.hao123.com/')  # 匹配字符串
print(match)                            # 打印匹配结果
pattern = 'https://(.*)'               # 表达式，“.*”获取www.hao123.com/
match = re.findall(pattern,'https://www.hao123.com/')  # 匹配字符串
print(match)                            # 打印匹配结果
