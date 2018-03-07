
# -*- coding: utf-8 -*-

"""
   切片连续，去掉文字头尾的空格
"""

def ktrim(s, ):
    i = 0
    n = len(s)
    if s[:1] != "" and s[:-1] != "":
        return s
    elif s[:1] == "":
        i = 1
    elif s[:-1] == "":
        n = n -1

    return ktrim(s[i:n])


def ztrim(s):
    lenstr = len(s)
    if lenstr == 0:
        return s
    else:
        ktrim(s)


if ztrim('hello  ') != 'hello':
    print('测试失败!')
elif ztrim('  hello') != 'hello':
    print('测试失败!')
elif ztrim('  hello  ') != 'hello':
    print('测试失败!')
elif ztrim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif ztrim('') != '':
    print('测试失败!')
elif ztrim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')