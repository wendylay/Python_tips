from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import numpy as np

# normal distribution center at x=0 and y=5
x = np.random.randn(100000)
y = np.random.randn(100000) + 5

plt.figure(figsize=(12.5, 10))
plt.hist2d(x, y, bins=100, norm=LogNorm(), cmap=plt.get_cmap('jet'))

font_format = {'family': 'Times New Roman',
               'size': 20,
               'color': 'k'}
cb = plt.colorbar()
cb.ax.tick_params(labelsize=16)

plt.xlabel('The x label', font_format)
plt.ylabel('The y label', font_format)
plt.xticks(fontproperties='Times', size=16)
plt.yticks(fontproperties='Times', size=16)
ax = plt.gca()
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)

plt.show()

