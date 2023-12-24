import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('grayscale')
# fivethrityeight
#ggplot
#matplotlib.org
x = np.arange(0, 30, 0.2)
y1 = np.sin(x)
y2 = np.cos(x)
# plt.grid(True)
# plt.title("Sine Function")
# # plt.suptitle('I am bigger')
#
# plt.xlabel("Weight of Students")
# plt.ylabel("height of Students")


plt.plot(x, y1, label="Sine")
plt.plot(x, y2, label="Cosine")

plt.legend(loc='lower right')
plt.show()