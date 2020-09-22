import numpy as np
import time
from scipy.special import erf
import matplotlib.pyplot as plt

mu = 0.02
ls = 50
ln = 50
sigma = np.linspace(0, 0.3, ls)
Ns = np.round_(np.logspace(0, 7, ln) + 1)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(11, 4))
fig.tight_layout(pad=3)

levels = np.linspace(40, 100, 7)
origin = 'lower'

#plu
n = 10000
str1 = "gs"
str3 = ".csv"
res1 = np.zeros((ls, ln))
for i in range(ls):
    str2 = str(i)
    with open(str1 + str2 + str3, 'r', encoding='utf-8-sig') as f:
        gs = np.genfromtxt(f, dtype=float, delimiter=',')
    for j in range(ln):
        #tmp1 = np.abs(gs[j, :] - )
        tmp2 = np.where(gs[j, :] > (np.log(1 + mu) - sigma[i] ** 2 / 4))
        res1[i, j] = len(tmp2[0]) / n

CS = axes[0].contourf(np.log10(Ns), sigma, 100 * res1, levels, origin=origin)
axes[0].contour(np.log10(Ns), sigma, 100 * res1, levels, colors=('k',), linewidths=(0.5,), origin=origin)
m1 = plt.cm.ScalarMappable()
m1.set_array(res1)
m1.set_clim(levels[0], 100)
CB = fig.colorbar(m1, boundaries=levels, ticks=levels, ax=axes[0])
CB.set_label(r'Fraction of $g_{{\langle\rangle}_N} > \mu -\sigma^2/4$ (%)')
axes[0].set_xlabel(r'$\log_{10}(N)$')
axes[0].set_ylabel(r'$\sigma$')
axes[0].set_title(r'$g_{{\langle\rangle}_N}$')
axes[0].set_xlim(1, 7)

#gdem
res2 = np.zeros((ls, ln))
for i in range(ls):
    for j in range(ln):
        res2[i, j] = 0.5 + 0.5 * erf(np.sqrt(Ns[j] / 32) * sigma[i])

CS = axes[1].contourf(np.log10(Ns), sigma, 100 * res2, levels, origin=origin)
axes[1].contour(np.log10(Ns), sigma, 100 * res2, levels, colors=('k',), linewidths=(0.5,), origin=origin)
m2 = plt.cm.ScalarMappable()
m2.set_array(res2)
m2.set_clim(levels[0], 100)
CB = fig.colorbar(m2, boundaries=levels, ticks=levels, ax=axes[1])
CB.set_label(r'Probability of $\bar{g}_{N} < \mu -\sigma^2/4$ (%)')
axes[1].set_xlabel(r'$\log_{10}(N)$')
axes[1].set_ylabel(r'$\sigma$')
axes[1].set_title(r'$\bar{g}_{N}$')
axes[1].set_xlim(1, 7)

plt.savefig("./../gbm_gplu_dem_contour.pdf", bbox_inches='tight')