import urllib.parse

encoding = urllib.parse.urlencode( [('activity','water ski'),('lake','Milford'),('code',52)] )
url = "http://www.example.com" + '?'+encoding
print(url)

