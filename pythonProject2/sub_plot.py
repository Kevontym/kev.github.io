import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100, 0.2)
y1 = np.sin(x)
y2 = x ** 2 + 2 * x
y3 = np.log(x)

# ax1 = plt.subplot(221)
# rows in window, 2nd difference colous, 3rd information index of subplot
# ax2 = plt.subplot(222)
# ax3 = plt.subplot(223)
# ax4 = plt.subplot(224)
#
# ax1.plot(x, y1)
# ax2.plot(x, y2)
# ax3.plot(x, y1, 'g')
# ax4.plot(x, y2, 'r')
# plt.tight_layout()
plt.figure(1)
ax1 = plt.subplot(211)
ax1 = plt.plot(x, y1, 'g')
ax2 = plt.subplot(212)
ax2 = plt.plot(x, y2, 'r')

plt.figure(2)
plt.plot(x, y2)

plt.figure(3)
plt.plot(x, y3)

plt.show()