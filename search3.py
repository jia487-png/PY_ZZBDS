import re                        # 导入re模块
pattern = r'\bmr\b'               # 表达式，mr两侧均有边界
match = re.search(pattern,'mrsoft')  # 匹配字符串,mr右侧不是边界是soft，匹配失败
print(match)                            # 打印匹配结果
match = re.search(pattern,'mr soft')  # 匹配字符串，mr左侧为边界右侧为空格，匹配成功
print(match)                            # 打印匹配结果
match = re.search(pattern,' mrsoft ')  # 匹配字符串，mr左侧为空格右侧为soft空格，匹配失败
print(match)                            # 打印匹配结果
match = re.search(pattern,'mr.soft')  # 匹配字符串，mr左侧为边界右侧为“.”，匹配成功
print(match)                            # 打印匹配结果
