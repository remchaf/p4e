from urllib.request import urlopen
import urllib.request
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.py4e.com/code3/mbox.txt?PHPSESSID=123447cb493a95f5ec285bfe56186dab'

dct = dict()
fhandler = urllib.request.urlopen(url, context=ctx)

for line in fhandler :
    if line.startswith('From ') :
        line = line.strip()
        email = line.split(' ')[1]
        dct['org'] = dct.get(email, 0) + 1
        
print(dct)