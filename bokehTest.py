import numpy as np
import bokeh.plotting as bkh
from bokeh.plotting import figure, output_file, show
bkh.output_notebook()
x = np.linspace(0., 1., 100)
y = np.cumsum(np.random.randn(100))
p=figure(title="example",x_axis_label='x',y_axis_label='y')
p.line(x, y, line_width=5)
show(p)


from bokeh.sampledata.iris import flowers
colormap = {'setosa': 'red',
'versicolor': 'green',
'virginica': 'blue'}
flowers['color'] = flowers['species'].map(lambda x: colormap[x])
k=figure(title="iris example")
k.scatter(flowers["petal_length"],
flowers["petal_width"],
color=flowers["color"],
fill_alpha=0.25, size=10,)
show(k)
