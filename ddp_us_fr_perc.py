import numpy as np
import matplotlib.pyplot as plt

# load data
grperc = np.genfromtxt('gr_perc.csv', delimiter=',')

#plot area
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(11, 4))
fig.tight_layout(pad=3)

#plot US incomes
axes[0].plot(grperc[:, 0], grperc[:, 4], LineStyle='-', lineWidth='2', label=r'Ensemble-average growth rate')
axes[0].plot(grperc[:, 0], grperc[:, 3], color='orangered',  LineStyle=(0, (1, 1)), lineWidth='2', label=r'Time-average growth rate')
axes[0].set_xlabel(r'Bottom percentile')
axes[0].set_ylabel(r'Growth between 1966 and 2014')
axes[0].set_ylim(0.1, 0.9)
axes[0].set_xlim(0, 100)
axes[0].set_xticks(np.arange(0, 101, step=5))
axes[0].legend(loc='upper left', fontsize='medium', frameon='False')
axes[0].set_title('United States')

#plot US incomes
axes[1].plot(grperc[:, 0], grperc[:, 2], LineStyle='-', lineWidth='2', label=r'Ensemble-average growth rate')
axes[1].plot(grperc[:, 0], grperc[:, 1], color='orangered',  LineStyle=(0, (1, 1)), lineWidth='2', label=r'Time-average growth rate')
axes[1].set_xlabel(r'Bottom percentile')
axes[1].set_ylabel(r'Growth between 1970 and 2015')
axes[1].set_ylim(0.4, 0.65)
axes[1].set_xlim(0, 100)
axes[1].set_xticks(np.arange(0, 101, step=5))
axes[1].legend(loc='lower left', fontsize='medium', frameon='False')
axes[1].set_title('France')

fig.savefig("./ddp_us_fr_perc.pdf", bbox_inches='tight')
plt.show()