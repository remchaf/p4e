import json
import urllib.request, urllib.parse
import ssl

sample_data = "http://py4e-data.dr-chuck.net/comments_42.json"
actual_data = "http://py4e-data.dr-chuck.net/comments_1582151.json"
url = input('Enter a url :')
if len(url) < 1 : url = sample_data
elif url == '3': url = actual_data

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

handle = urllib.request.urlopen(url, context=ctx)

count = 0
data = json.loads(handle.read().decode())
for di in data["comments"] :
    count += int(di["count"])

print("Sumup to :", count)