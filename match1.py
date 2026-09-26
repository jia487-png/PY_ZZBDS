import re
pattern = r'mr_\w+'                       # 表达式字符串
string = 'MR_SHOP mr_shop'              # 要匹配的字符串
match = re.match(pattern,string,re.I)  # 匹配字符串，不区分大小写
print(match)                              # 输出匹配结果
string = '项目名称MR_SHOP mr_shop'
match = re.match(pattern,string,re.I)  # 匹配字符串，不区分大小写
print(match)                              # 输出匹配结果

pattern = r'mr_\w*'                       # 表达式字符串
string = 'MR_SHOP mr_shop'              # 要匹配的字符串
match = re.match(pattern,string,re.I)  # 匹配字符串，不区分大小写
print(match)                              # 输出匹配结果
string = '项目名称MR_SHOP mr_shop'
match = re.match(pattern,string,re.I)  # 匹配字符串，不区分大小写
print(match)                              # 输出匹配结果