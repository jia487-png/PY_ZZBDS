import re                        # 导入re模块
# 表达式，(\d?)+表示多个数字可有可无，\s空格可有可无，([\u4e00-\u9fa5]?)+多个汉字可有可无
pattern = r'(\d?)+mrsoft\s?([\u4e00-\u9fa5]?)+'
match = re.search(pattern,'01mrsoft')  # 匹配字符串,mrsoft前有01数字，匹配成功
print(match)                            # 打印匹配结果
match = re.search(pattern,'mrsoft')  # 匹配字符串，mrsoft匹配成功
print(match)                            # 打印匹配结果
match = re.search(pattern,'mrsoft ')  # 匹配字符串，mrsoft后面有一个空格，匹配成功
print(match)                            # 打印匹配结果
match = re.search(pattern,'mrsoft 第一')  # 匹配字符串，mrsoft后面有空格和汉字，匹配成功
print(match)                            # 打印匹配结果
match = re.search(pattern,'rsoft 第一')  # 匹配字符串，rsoft后面有空格和汉字，匹配失败
print(match)                            # 打印匹配结果