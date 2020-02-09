import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'arial'
plt.rcParams['font.size'] = 18
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.major.width'] = 1.0
plt.rcParams['ytick.major.width'] = 1.0
plt.rcParams['lines.linewidth'] = 0.8

plt.grid(which='major',color='lightgray',linestyle='--')
plt.grid(which='minor',color='lightgray',linestyle='--')

npg = mpl.colors.ListedColormap(['#E64B3599','gold','limegreen','darkturquoise','indigo'])
