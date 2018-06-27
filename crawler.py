from urllib.request import urlopen
import webbrowser as wb

a = urlopen("http://www.naver.com")
f = open("ex.html", "wt", encoding='utf-8')
print(a.read().decode(), file=f)
f.close()

wb.open("ex.html")
