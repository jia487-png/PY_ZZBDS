# PY_ZZBDS
正则表达式


# match()匹配     从第一个字符开始匹配

## pattern = r'mr_\w+'                       # 表达式字符串
匹配以mr_开头的字符串，不是以mr_不会匹配


## 匹配值的返回定义
~~~~
import re
pattern = r'mr_\w+'                       # 模式字符串
string = 'MR_SHOP mr_shop mr_jps'              # 要匹配的字符串
match = re.match(pattern,string,re.I)  # 匹配字符串，不区分大小写
print('匹配值的起始位置：',match.start())
print('匹配值的结束位置：',match.end())
print('匹配位置的元组：',match.span())
print('要匹配的字符串：',match.string)
print('匹配数据：',match.group())
~~~~

## 输出结果
匹配值的起始位置： 0    
匹配值的结束位置： 7    
匹配位置的元组： (0, 7)    
要匹配的字符串： MR_SHOP mr_shop mr_jps    
匹配数据： MR_SHOP    

## pattern = r'.ello'                 # 表达式
匹配第一个任意开头的ello字符串，ello前面只能有一个字符

## pattern = r'hello|我'                 # 表达式,表示需要匹配“hello”或“我”开头的字符串
匹配多个字符串，但仍从第一个字符开始匹配

## pattern = r'hello\s(\w+)'
表达式，“hello”开头，“\s”中间空格，“（\w+）”分组后面所有字母、数字以及下划线数据

## pattern = r'h\w+\s[\u4e00-\u9fa5]+\s\w+n$'
表达式,h开头，n$表示n结尾


# search()    获取第一匹配值

## pattern = r'mr_\w+'                       # 模式字符串
返回第一个匹配的位置，不是从0开始的，从任何位置都可以

## pattern = r'\bmr\b'               
表达式，mr两侧均有边界

# findall()  匹配所有指定字符开头字符串

## pattern = r'mr_\w+'                        
匹配出以mr_开头的所有模式字符串

## pattern = r'https://.*/'         
贪婪匹配

## pattern = 'https://.*(\d+).com/'               # 表达式，“.*”获取www.hao123.com
## pattern = 'https://.*?(\d+).com/'               # 表达式，“.*”获取www.hao123.com
## pattern = 'https://(.*?)'               # 表达式，“.*?”获取www.hao123.com/
## pattern = 'https://(.*)'               # 表达式，“.*”获取www.hao123.com/
非贪婪匹配

