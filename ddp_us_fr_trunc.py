import numpy as np
import matplotlib.pyplot as plt

# load data
with open('US_trunc.csv', 'r', encoding='utf-8-sig') as f:
    US = np.genfromtxt(f, dtype=float, delimiter=',')
with open('FR_trunc.csv', 'r', encoding='utf-8-sig') as f:
    FR = np.genfromtxt(f, dtype=float, delimiter=',')

# right currency normalisation
USD2014 = 71014
US_fac = USD2014 / US[-1, 5]
USDTOEUR2019 = 1.12
EUR2014 = 35222
FR_fac = EUR2014 * USDTOEUR2019 / FR[-1, 5]

#plot area
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(11, 8))
fig.tight_layout(pad=3)

#plot US rates
l=len(US[:, 0])
axes[0, 0].axhline(y=0.0, Color='black', LineStyle=(0, (5, 15)), lineWidth='0.5')
axes[0, 0].plot(US[0:l, 0], US[0:l, 3], LineStyle='-', lineWidth='2', label=r'Ensemble-average growth rate')
axes[0, 0].plot(US[0:l, 0], US[0:l, 4], color='orangered', LineStyle=(0, (1, 1)), lineWidth='2', label=r'Time-average growth rate')
axes[0, 0].set_title('United States')
axes[0, 0].set_xlabel(r'Year')
axes[0, 0].set_ylabel(r'Annual growth rate')
axes[0, 0].set_ylim(-0.085, 0.085)
axes[0, 0].set_yticks(np.arange(-0.08, 0.09, step=0.02))
axes[0, 0].set_xlim(1963, 2017)
axes[0, 0].set_xticks(np.arange(1965, 2020, step=5))
axes[0, 0].legend(loc='lower left', fontsize='medium', frameon='False')

#plot FR rates
l=len(FR[:, 0])
axes[0, 1].axhline(y=0.0, Color='black', LineStyle=(0, (5, 15)), lineWidth='0.5')
axes[0, 1].plot(FR[0:l, 0], FR[0:l, 3], LineStyle='-', lineWidth='2', label=r'Ensemble-average growth rate')
axes[0, 1].plot(FR[0:l, 0], FR[0:l, 4], color='orangered', LineStyle=(0, (1, 1)), lineWidth='2', label=r'Time-average growth rate')
axes[0, 1].set_title('France')
axes[0, 1].set_xlabel(r'Year')
axes[0, 1].set_ylabel(r'Annual growth rate')
axes[0, 1].set_ylim(-0.085, 0.085)
axes[0, 1].set_yticks(np.arange(-0.08, 0.09, step=0.02))
axes[0, 1].set_xlim(1963, 2017)
axes[0, 1].set_xticks(np.arange(1965, 2020, step=5))
axes[0, 1].legend(loc='lower left', fontsize='medium', frameon='False')

#plot US incomes
axes[1, 0].plot(US[:, 0], US[:, 7] * US_fac, LineStyle='-', lineWidth='2', label=r'GDP per capita')
axes[1, 0].plot(US[:, 0], US[:, 8] * US_fac, color='orangered', LineStyle=(0, (1, 1)), lineWidth='2', label=r'DDP per capita')
axes[1, 0].set_xlabel(r'Year')
axes[1, 0].set_ylabel(r'Income (2019 $/year)')
axes[1, 0].set_ylim(7500, 82500)
axes[1, 0].set_yticks(np.arange(10000, 81000, step=10000))
axes[1, 0].set_xlim(1963, 2017)
axes[1, 0].set_xticks(np.arange(1965, 2020, step=5))
axes[1, 0].legend(loc='upper left', fontsize='medium', frameon='False')

#plot FR incomes
axes[1, 1].plot(FR[:, 0], FR[:, 7] * FR_fac, LineStyle='-', lineWidth='2', label=r'GDP per capita')
axes[1, 1].plot(FR[:, 0], FR[:, 8] * FR_fac, color='orangered', LineStyle=(0, (1, 1)), lineWidth='2', label=r'DDP per capita')
axes[1, 1].set_xlabel(r'Year')
axes[1, 1].set_ylabel(r'Income (2019 $/year)')
axes[1, 1].set_ylim(7500, 82500)
axes[1, 1].set_yticks(np.arange(10000, 81000, step=10000))
axes[1, 1].set_xlim(1963, 2017)
axes[1, 1].set_xticks(np.arange(1965, 2020, step=5))
axes[1, 1].legend(loc='upper left', fontsize='medium', frameon='False')

fig.savefig("./ddp_us_fr_trunc.pdf", bbox_inches='tight')
plt.show()