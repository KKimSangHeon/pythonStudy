from wordcloud import WordCloud, STOPWORDS

import numpy as np
from PIL import Image
text = open('alice.txt').read()
alice_mask = np.array(Image.open('heart.jpg'))

stopwords = set(STOPWORDS)
stopwords.add("said")
import matplotlib.pyplot as plt
import platform

path = "c:/Windows/Fonts/malgun.ttf"
from matplotlib import font_manager, rc
if platform.system() == 'Darwin' :
    rc('font', fiamily='AppleGothic')
elif platform.system() == 'Windows' :
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unkonown system.. sorry')

plt.figure(figsize=(8,8))
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()

wc = WordCloud(background_color='white', max_words=2000, mask=alice_mask, stopwords = stopwords)
wc = wc.generate(text)
wc.words_

plt.figure(figsize=(12,12))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()