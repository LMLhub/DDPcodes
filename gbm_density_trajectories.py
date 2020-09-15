import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stat
from scipy.integrate import cumtrapz
import scipy.optimize as opt

origin = 'lower'

sigma = 0.2
mu = 0.05
initval = 10000

t = np.linspace(0.0, 30.0, num=2500)
nt = len(t)
dt = t[nt - 1] - t[nt - 2]
ntraj = 200
means = np.zeros([nt, 1])
medians = np.zeros([nt, 1])
m = np.zeros([nt, 1])
s = np.zeros([nt, 1])
trajs = np.ones([nt, ntraj])

for i in range(nt):
    means[i] = np.exp(mu * t[i])
    medians[i] = np.exp((mu - sigma**2 / 2) * t[i])
    s[i] = sigma * np.sqrt(t[i])
    m[i] = ((mu - sigma ** 2 / 2) * t[i])
    if i < nt - 1:
        noise = np.random.randn(1, ntraj)
        trajs[i + 1, :] = trajs[i, :] * (1 + mu * dt + (sigma * np.sqrt(dt)) * noise)

#plot area
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(11, 4))
fig.tight_layout(pad=3)

h0 = axes[0].semilogy(t, trajs * initval, Color='0.5', alpha=0.25, LineStyle='-', lineWidth='0.5')
hh0 = axes[0].semilogy(t, np.mean(trajs, 1) * initval, LineStyle='-', lineWidth='4', label=r'GDP per capita')
hh1 = axes[0].semilogy(t, stat.gmean(trajs, 1) * initval, color='orangered', LineStyle=(0, (1, 1)), lineWidth='4', label=r'DDP per capita')
axes[0].set_xlabel(r'Time (years)')
axes[0].set_ylabel(r'Income ($/year)')
axes[0].set_xlim(0, 30)
axes[0].set_ylim(2000, 3*10**5)
axes[0].legend(loc='upper left', fontsize='medium', frameon='False')

A1 = axes[1].fill_between(t, np.transpose(medians[:, 0] * initval), np.transpose(np.exp(np.log(medians[:, 0]) + s[:, 0]) * initval), facecolor='k', alpha=0.2)
A2 = axes[1].fill_between(t, np.transpose(np.exp(np.log(medians[:, 0]) - s[:, 0]) * initval), np.transpose(medians[:, 0] * initval), facecolor='k', alpha=0.2)
A3 = axes[1].fill_between(t, np.transpose(np.exp(np.log(medians[:, 0]) - (2 * s[:, 0])) * initval), np.transpose(medians[:, 0] * initval), facecolor='k', alpha=0.2)
A4 = axes[1].fill_between(t, np.transpose(medians[:, 0] * initval), np.transpose(np.exp(np.log(medians[:, 0]) + (2 * s[:, 0])) * initval), facecolor='k', alpha=0.2)
hh0 = axes[1].semilogy(t, means * initval, LineStyle='-', lineWidth='4', label=r'GDP per capita')
hh1 = axes[1].semilogy(t, medians * initval, color='orangered', LineStyle=(0, (1, 1)), lineWidth='4', label=r'DDP per capita')
axes[1].legend(loc='upper left', fontsize='medium', frameon='False')
axes[1].set_xlabel(r'Time (years)')
axes[1].set_ylabel(r'Income ($/year)')
axes[1].set_xlim(0, 30)
axes[1].set_ylim(2000, 3*10**5)

plt.savefig("./gbm_density_trajectories.png", dpi=400, bbox_inches='tight')
plt.show()