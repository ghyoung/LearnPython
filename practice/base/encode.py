#ord()查看Unicode
myChar = '我'
print('"我"的编码是： ', ord(myChar))

#chr()查看编码对应的字符
myCode = 25105
print('"25105"代表了： ', chr(myCode))

#encode()编码
print(myChar.encode())
