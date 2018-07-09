import numpy as np
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
import matplotlib
boston = load_boston()
x = boston.data
y = boston.target
lr = LinearRegression()
lr.fit(x,y)
rmse = np.sqrt(lr._residues/len(x))
print('RMSE: {}'.format(rmse))
fig, ax = plt.subplots()
ax.plot([0,50],[0,50],'-',color=(.9,.3,.3), lw=4)

ax.scatter(lr.predict(x), boston.target)
matplotlib.rc('font', family='HYSinMyeongJo-Medium')
ax.set_xlabel(u'예측가격')
ax.set_ylabel(u'실제주택가격')
fig.savefig('Figure_09_08.png')
plt.show()


import matplotlib.font_manager as fm
font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')
f = [f.name for f in fm.fontManager.ttflist]
print(f)

from collections import OrderedDict
from IPython.display import (display, clear_output, YouTubeVideo)
from ipywidgets import Dropdown

dw = Dropdown(options=OrderedDict([('SciPy 2016', 'Ejh0ftSjk6g'), ('PyCon 2016', 'YgtL4S7Hrwo')]))

from collections import OrderedDict
from IPython.display import (display, clear_output, YouTubeVideo)
from ipywidgets import Dropdown

dw = Dropdown(options=OrderedDict([('SciPy 2016', 'Ejh0ftSjk6g'), ('PyCon 2016', 'YgtL4S7Hrwo')]))


def on_value_change(name, val):
    clear_output()
    display(YouTubeVideo(val))


dw.on_trait_change(on_value_change, 'value')
dw.value = dw.options['SciPy 2016']
display(dw)
