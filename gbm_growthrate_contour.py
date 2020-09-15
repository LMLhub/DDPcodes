import numpy as np
import matplotlib.pyplot as plt

mu = 0.02
ls = 25
ln = 25
sigma = np.linspace(0, 0.3, ls)
Ns = np.round_(np.logspace(0, 7, ln) + 1)
sigsig = 2
n = 10000
res = np.zeros((ls, ln))
for j in range(ln):
    N = int(Ns[j])
    for i in range(n):
        noise = np.random.randn(N, 1)
        tmp = np.exp(sigsig * noise)
        tmp1 = np.sum(tmp ** 2)
        tmp2 = np.sum(tmp) ** 2
        res[:, j] = res[:, j] + (1/n) * (- 100 * (0.5 * sigma ** 2) * (np.mean(tmp1 / tmp2)) / mu)

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(5.5, 4))
levels = [-200,-150,-100,-50,-25,-20,-15,-10,-5,-4,-3,-2,-1,-0.5,0]
origin = 'lower'

CS = plt.contourf(np.log10(Ns), sigma, res, levels, origin=origin)
plt.contour(np.log10(Ns), sigma, res, levels, colors=('k',), linewidths=(0.5,), origin=origin)
m = plt.cm.ScalarMappable()
m.set_array(res)
m.set_clim(levels[0], 0)
CB = fig.colorbar(m, boundaries=levels, ticks=levels[::2])
CB.set_label(r'Deviation of $\frac{\langle\mathrm{d} \log\langle x \rangle_N\rangle}{\mathrm{dt}}$ from $\mu$ (%)')
axes.set_xlabel(r'$\log_{10}(N)$')
axes.set_ylabel(r'$\sigma$')

plt.savefig("./gbm_growthrate_contour.pdf", bbox_inches='tight')