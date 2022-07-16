from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sample = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
actual = "http://py4e-data.dr-chuck.net/known_by_Aimie.html"
position, procss = None, None
url = input("Enter the url :")
if len(url) == 0 :
    url = sample
    position, procss = 3, 4
elif url == '3' :
    url = actual
    position, procss = 18, 7


for item in range(procss):
    soup = BeautifulSoup(urlopen(url, context=ctx).read(), "html.parser")    
    a = soup('a')
    if item == procss - 1 :
        print(a[position - 1].text)
        break
    
    url = a[position - 1].get("href", None)
    print(url)
    