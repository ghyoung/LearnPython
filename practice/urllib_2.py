import urllib.parse
import urllib.request

date = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')

response = urllib.request.urlopen('http://httpbin.org/post', data=date)
print(response.read())
