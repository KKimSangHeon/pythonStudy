import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

np.random.seed(12)
plt.pcolormesh(np.random.rand(16, 16))
plt.colorbar()
np.random.seed(12)
plt.pcolormesh(np.random.rand(16, 16))



x1 = np.random.randn(80)
x2 = np.random.randn(80)
x3 = x1 * x2
y1 = .5 + 2 * x1 - x2 + 2.5 * x3 + 3 * np.random.randn(80)
y2 = .5 + 2 * x1 - x2 + 2.5 * np.random.randn(80)
y3 = y2 + np.random.randn(80)
sns.violinplot([x1,x2, x3])
plt.show()
sns.regplot(x2, y2)
plt.show()
df = pd.DataFrame(dict(x1=x1, x2=x2, x3=x3,y1=y1, y2=y2, y3=y3))
plt.show()
sns.pairplot(df)
plt.show()
