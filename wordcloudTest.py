from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = open('consitution.txt').read()
wordcloud = WordCloud().generate(text)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()