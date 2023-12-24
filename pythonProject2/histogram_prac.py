import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 172, 8
x = mu + sigma * np.random.randn(10000)


plt.hist(x, 100, facecolor='b', density=True)
plt.xlabel("Heights")
plt.ylabel("Percentages of Students")
plt.title("Height of Students")
plt.text(145, 0.04, "µ = 172, sig = 8")
plt.grid(True)
plt.show()