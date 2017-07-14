import urllib.request
import re

url = "https://list.jd.com/list.html?cat=9987,653,655"
req = urllib.request.Request(url)
data = urllib.request.urlopen(req).read()

patten = "<li class=\"gl-item\">.*</li>"
re.compile(patten)

res = re.search(patten, data.decode(), re.S)
print(res)