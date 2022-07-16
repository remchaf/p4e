# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sample_data = "http://py4e-data.dr-chuck.net/comments_42.html"
actual_data = "http://py4e-data.dr-chuck.net/comments_1582148.html"

url = input('Enter url - ')
if len(url) < 1 : url = sample_data
elif url == '3' : url = actual_data

html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
s = 0

for tag in tags:
    s += int(tag.text)
    
print(s)