#格式化操作
formatStr = 'I like {0} and {1}'.format('Swisse','Rock')
print(formatStr)
# 默认是左对齐，20表示占位的长度
formatStr = 'I like {0:20} and {1}'.format('Swisse','Rock')
print(formatStr)
# ^表示居中对齐
formatStr = 'I like {0:^20} and {1}'.format('Swisse','Rock')
print(formatStr)
# >表示右对齐
formatStr = 'I like {0:>20} and {1}'.format('Swisse','Rock')
print(formatStr)
# 截取第一个位置的前2个字符
formatStr = 'I like {0:.2} and {1}'.format('Swisse','Rock')
print(formatStr)
# 占位20，但是只取前2个字符
formatStr = 'I like {0:20.2} and {1}'.format('Swisse','Rock')
print(formatStr)
# 将截取和对齐方向结合起来用
formatStr = 'I like {0:^20.2} and {1}'.format('Swisse','Rock')
print(formatStr)

#——————————————————————————————————————————————————————————————————
# 传递数字
formatStr = 'Rock is  {0} yeas and {1}cm tall'.format(35,198.2134)
print(formatStr)
# d为整数，f浮点数
# 5表示占位，8.1f共占8位但只保留1位小数
formatStr = 'Rock Is  {0:<5d} yeas and {1:8.1f}cm tall'.format(35,198.2134)
print(formatStr)

#——————————————————————————————————————————————————————————————————
# 是否全为字母
print(formatStr.isalpha())
# 默认按照空格分割
print(formatStr.split())
# 用指定字符分割
URL = ' www.baidu.com '
splitURL = URL.split('.')
print(splitURL)

#——————————————————————————————————————————————————————————————————
print(URL)
# 去掉字符串中的左边空格
print(URL.rstrip())
# 去掉字符串中的首尾空格
print(URL.strip())

#——————————————————————————————————————————————————————————————————
#将字符全部转换为大写
FS = formatStr.upper()
print('FS的值： ',FS)
#判断是否为大些
print('据说FS里面全是大写的？', FS.isupper())
#字符全部转换为小写
fs = FS.lower()
print('fs的值：',fs)
#将字符串的首字母变为大写
fS = fs.capitalize()
print('fS的值:', fS)
#所有单词的首字母大写？
print(formatStr, '中的所有单词都是首字母大写?', formatStr.istitle())
#将每个单词变成首字母大写
print('把formatStr格式化成所有单词首字母大写?', formatStr.title())

#join函数连接
joinURL = '--'.join(splitURL)
print(joinURL)
