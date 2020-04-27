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

npg = mpl.colors.ListedColormap(['#E64B3599','#4DBBD599','#00A08799','#3C548899','#F39B7F99','#8491B499','#91D1C299','#DC000099','#7E614899','#B09C8599'])
npg_clist = ['#E64B35FF','#4DBBD5FF','#00A087FF','#3C5488FF','#F39B7FFF','#8491B4FF','#91D1C2FF','#DC0000FF','#7E6148FF','#B09C85FF']
npg_clist06 = ['#E64B3599','#4DBBD599','#00A08799','#3C548899','#F39B7F99','#8491B499','#91D1C299','#DC000099','#7E614899','#B09C8599']
