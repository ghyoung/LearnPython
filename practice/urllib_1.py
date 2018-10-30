import urllib.request

response1 = urllib.request.urlopen("https://www.baidu.com")
print(type(response1))
print(type(response1.getheaders()))
print(response1.getheaders())
print(response1.getheader("Server"))
print(response1.status)
print(response1.readline())
print(response1.geturl())
print('\n')
print(response1.read().decode('utf-8'))
