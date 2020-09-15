import numpy as np
import matplotlib.pyplot as plt

# load data
with open('US_growthrates_limits.csv', 'r', encoding='utf-8-sig') as f:
    US = np.genfromtxt(f, dtype=float, delimiter=',')
with open('FR_growthrates_limits.csv', 'r', encoding='utf-8-sig') as f:
    FR = np.genfromtxt(f, dtype=float, delimiter=',')

# right currency normalisation
US_fac = 1.2097981680721106
FR_fac = 1.1672329668221808

#plot area
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(11, 8))
fig.tight_layout(pad=3)

#plot US rates
l=len(US[:, 0])
axes[0, 0].axhline(y=0.0, Color='black', LineStyle=(0, (5, 15)), lineWidth='0.5')
axes[0, 0].plot(US[0:l, 0], US[0:l, 1], color='orangered', LineStyle='-', lineWidth='2', label=r'Time-average growth rate')
axes[0, 0].plot(US[0:l, 0], US[0:l, 2], 'k', LineStyle='--', lineWidth='2', label=r'Lower thresholds')
axes[0, 0].plot(US[0:l, 0], US[0:l, 3], 'k', LineStyle=':', lineWidth='2', label=r'Upper thresholds')
axes[0, 0].set_title('United States')
axes[0, 0].set_xlabel(r'Year')
axes[0, 0].set_ylabel(r'Annual growth rate')
axes[0, 0].set_ylim(-0.21, 0.21)
axes[0, 0].set_yticks(np.arange(-0.20, 0.21, step=0.05))
axes[0, 0].set_xlim(1963, 2017)
axes[0, 0].set_xticks(np.arange(1965, 2020, step=5))
axes[0, 0].legend(loc='lower left', fontsize='medium', frameon='False')

#plot US incomes
axes[1, 0].plot(US[:, 0], US_fac * US[:, 4], color='orangered', LineStyle='-', lineWidth='2', label=r'DDP per capita')
axes[1, 0].plot(US[:, 0], US_fac * US[:, 5], 'k', LineStyle='--', lineWidth='2', label=r'Lower thresholds')
axes[1, 0].plot(US[:, 0], US_fac * US[:, 6], 'k', LineStyle=':', lineWidth='2', label=r'Upper thresholds')
axes[1, 0].set_xlabel(r'Year')
axes[1, 0].set_ylabel(r'Income (2019 USD/year)')
axes[1, 0].set_ylim(7500, 82500)
axes[1, 0].set_yticks(np.arange(10000, 81000, step=10000))
axes[1, 0].set_xlim(1963, 2017)
axes[1, 0].set_xticks(np.arange(1965, 2020, step=5))
axes[1, 0].legend(loc='upper left', fontsize='medium', frameon='False')

#plot FR rates
l=len(FR[:, 0])
axes[0, 1].axhline(y=0.0, Color='black', LineStyle=(0, (5, 15)), lineWidth='0.5')
axes[0, 1].plot(FR[0:l, 0], FR[0:l, 1], color='orangered', LineStyle='-', lineWidth='2', label=r'Time-average growth rate')
axes[0, 1].plot(FR[0:l, 0], FR[0:l, 2], 'k', LineStyle='--', lineWidth='2', label=r'Lower thresholds')
axes[0, 1].plot(FR[0:l, 0], FR[0:l, 3], 'k', LineStyle=':', lineWidth='2', label=r'Upper thresholds')
axes[0, 1].set_title('France')
axes[0, 1].set_xlabel(r'Year')
axes[0, 1].set_ylabel(r'Annual growth rate')
axes[0, 1].set_ylim(-0.21, 0.21)
axes[0, 1].set_yticks(np.arange(-0.20, 0.21, step=0.05))
axes[0, 1].set_xlim(1963, 2017)
axes[0, 1].set_xticks(np.arange(1965, 2020, step=5))
axes[0, 1].legend(loc='lower left', fontsize='medium', frameon='False')

#plot FR incomes
axes[1, 1].plot(FR[:, 0], FR_fac * FR[:, 4], color='orangered', LineStyle='-', lineWidth='2', label=r'DDP per capita')
axes[1, 1].plot(FR[:, 0], FR_fac * FR[:, 5], 'k', LineStyle='--', lineWidth='2', label=r'Lower thresholds')
axes[1, 1].plot(FR[:, 0], FR_fac * FR[:, 6], 'k', LineStyle=':', lineWidth='2', label=r'Upper thresholds')
axes[1, 1].set_xlabel(r'Year')
axes[1, 1].set_ylabel(r'Income (2019 USD/year)')
axes[1, 1].set_ylim(7500, 82500)
axes[1, 1].set_yticks(np.arange(10000, 81000, step=10000))
axes[1, 1].set_xlim(1963, 2017)
axes[1, 1].set_xticks(np.arange(1965, 2020, step=5))
axes[1, 1].legend(loc='upper left', fontsize='medium', frameon='False')

fig.savefig("./ddp_us_fr_lims.pdf", bbox_inches='tight')
plt.show()