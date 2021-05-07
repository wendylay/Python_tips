from matplotlib import pyplot as plt
import numpy as np
"""refer: https://www.bilibili.com/read/cv3307847/"""

x = np.linspace(0, 3 * np.pi, 40)
y1 = np.sin(x)
y2 = 0.1 * x - 0.5

plt.figure(figsize=(12.5, 10))
# 线条颜色black, 线宽2, 标记大小13, 标记填充颜色从网上找16进制好看的颜色
plt.plot(x, y1, '-o', color='black', markersize=13, markerfacecolor='#44cef6', linewidth=2)
plt.plot(x, y2, '-o', color='black', markersize=13, markerfacecolor='#e29c45', linewidth=2)

# 字体设置: 字体名称Times New Roman, 字体大小34
font_format = {'family': 'Times New Roman', 'size': 34}
plt.xlabel('Time (s)', font_format)
plt.ylabel('Displacement (m)', font_format)

# 设置坐标轴 x范围0~3*pi, y范围-1.2~1.2
plt.axis([0, 3 * np.pi, -1.2, 1.2])

# 横纵坐标上的字体大小与类型(不是xlabel, 是xticks)
plt.xticks(fontproperties='Times New Roman', size=34)
plt.yticks(fontproperties='Times New Roman', size=34)

# 整个图像与展示框的相对位置
plt.subplots_adjust(left=0.19, right=0.94, bottom=0.13)

# 调整上下左右四个边框的线宽为2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)

plt.show()
