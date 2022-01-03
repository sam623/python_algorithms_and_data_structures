import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 100., 1)
log_n = np.log2(n)



plt.plot(n, np.ones(len(n)),'green')
plt.text(90,2.5,r"$\mathit{O(1)}$")
plt.plot(n, log_n,c='#009900')
plt.text(85,9,r"$\mathit{O(log_2\ n)}$")
plt.plot(n, n,'b')
plt.text(85,93,r"$\mathit{O(n)}$")
plt.plot(n, n* log_n,'orange')
plt.text(22,95,r"$\mathit{O(n\ log_2\ n)}$")
plt.plot(n, n**2, c='#FF3333')
plt.text(10,95,r"$\mathit{O(n^2)}$")
plt.plot(n, 2**n, c='#CC0000')
plt.text(-1,95,r"$\mathit{O(2^n)}$")
plt.xlabel(r"$\mathit{n}$")
plt.ylabel("Operations")
plt.xlim([-1, 99])
plt.ylim([-1, 101])

ax = plt.gca()
ax.axes.xaxis.set_ticks([])
ax.axes.yaxis.set_ticks([])

plt.show()
