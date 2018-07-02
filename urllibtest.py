import sys, urllib.request
page = "http://www.example.com"
req = urllib.request.Request(page)
fd = urllib.request.urlopen(req,)
while 1:
    data = fd.read(1024)
    if not len(data):
        break
    sys.stdout.write(data.decode())