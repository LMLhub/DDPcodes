import numpy as np
import matplotlib.pyplot as plt

# load data
with open('US_trunc.csv', 'r', encoding='utf-8-sig') as f:
    US = np.genfromtxt(f, dtype=float, delimiter=',')
with open('FR_trunc.csv', 'r', encoding='utf-8-sig') as f:
    FR = np.genfromtxt(f, dtype=float, delimiter=',')
with open('US_growthrates.csv', 'r', encoding='utf-8-sig') as f:
    US2 = np.genfromtxt(f, dtype=float, delimiter=',')
with open('FR_growthrates.csv', 'r', encoding='utf-8-sig') as f:
    FR2 = np.genfromtxt(f, dtype=float, delimiter=',')

# right currency normalisation
USD2014 = 71014
US_fac = USD2014 / US[-1, 5]
USDTOEUR2019 = 1.12
EUR2014 = 35222
FR_fac = EUR2014 * USDTOEUR2019 / FR[-1, 5]

#plot area
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(11, 4.5))
fig.tight_layout(pad=5)

#plot US rates
l = len(US[:, 0])
l1 = axes[0].plot(US2[:, 0], 100 * US2[:, 8], 'k', LineStyle='-', lineWidth='2', label=r'Top 10% income share')
axes[0].set_title('United States')
axes[0].set_xlabel(r'Year')
axes[0].set_ylabel(r'Income share (%)')
axes[0].set_ylim(0, 50)
axes[0].set_yticks(np.arange(0, 51, step=5))
axes[0].set_xlim(1963, 2017)
axes[0].set_xticks(np.arange(1965, 2020, step=5))
ax2 = axes[0].twinx()
ax2.set_ylabel(r'Ergodicity gap')
l2 = ax2.plot(US[:, 0], np.log(US[:, 7] * US_fac) - np.log(US[:, 8] * US_fac), Color='0.4',  LineStyle=(0, (1, 1)), lineWidth='2', label=r'Ergodicity gap')
ax2.set_ylim(0, 0.45)
ax2.set_yticks(np.arange(0, 0.49, step=0.05))
h1, l1 = axes[0].get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
axes[0].legend(h1+h2, l1+l2, loc='lower right',  fontsize='medium', frameon='False')

#plot FR rates
l = len(FR[:, 0])
l1 = axes[1].plot(FR2[:, 0], 100 * FR2[:, 8], 'k', LineStyle='-', lineWidth='2', label=r'Top 10% income share')
axes[1].set_title('France')
axes[1].set_xlabel(r'Year')
axes[1].set_ylabel(r'Income share (%)')
axes[1].set_ylim(0, 50)
axes[1].set_yticks(np.arange(0, 51, step=5))
axes[1].set_xlim(1963, 2017)
axes[1].set_xticks(np.arange(1965, 2020, step=5))
ax2 = axes[1].twinx()
ax2.set_ylabel(r'Ergodicity gap')
l2 = ax2.plot(FR[:, 0], np.log(FR[:, 7] * FR_fac) - np.log(FR[:, 8] * FR_fac), Color='0.4',  LineStyle=(0, (1, 1)), lineWidth='2', label=r'Ergodicity gap')
ax2.set_ylim(0, 0.45)
ax2.set_yticks(np.arange(0, 0.49, step=0.05))
h1, l1 = axes[1].get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
axes[1].legend(h1+h2, l1+l2, loc='lower right',  fontsize='medium', frameon='False')

fig.savefig("./top10_gap.pdf", bbox_inches='tight')
plt.show()