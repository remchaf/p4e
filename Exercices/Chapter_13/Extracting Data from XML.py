import urllib.request, urllib.parse
import xml.etree.ElementTree as ET
import ssl

sample_data = 'http://py4e-data.dr-chuck.net/comments_42.xml'
actual_data = 'http://py4e-data.dr-chuck.net/comments_1582150.xml'

url = input("Enter a url :")
if len(url) < 1 : url = sample_data
elif url == '3' : url = actual_data

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

h = urllib.request.urlopen(url, context=ctx)
tree = ET.fromstring(h.read().decode())

c = 0
for count in tree.findall('./comments/comment/count') :
    c += int(count.text)

print(c)