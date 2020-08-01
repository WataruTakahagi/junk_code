import numpy as np
import pandas as pd
import math
from pylab import *
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as ticker
from matplotlib.ticker import ScalarFormatter
import matplotlib
matplotlib.font_manager._rebuild()

npg_clist = ['#E64B35FF','#4DBBD5FF','#00A087FF','#3C5488FF','#F39B7FFF','#8491B4FF','#91D1C2FF','#DC0000FF','#7E6148FF','#B09C85FF'] #NPG Journal Color Palettes (https://nanx.me/ggsci/index.html)

plt.rcParams['font.family']= 'sans-serif'
plt.rcParams['font.sans-serif'] = ['arial']
plt.rcParams['font.size'] = 15
plt.rcParams['xtick.direction'] = 'out'
plt.rcParams['ytick.direction'] = 'out'
plt.rcParams['xtick.major.width'] = 0.5
plt.rcParams['ytick.major.width'] = 0.5
plt.rcParams['axes.linewidth'] = 0.5

plt.grid(which='major',color='lightgray',linestyle='--')#Major Grid
plt.grid(which='minor',color='lightgray',linestyle='--')#Minor Grid

#y-Axis Scientific notation
ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.ticklabel_format(style="sci",  axis="y",scilimits=(0,0))

#Delete Axis label
ax.tick_params(labelbottom=False,labelleft=False,labelright=False,labeltop=False)

#Delete Axis
ax.tick_params(bottom=False,left=False,right=False,top=False)

#Save figure without margin
plt.savefig('figure.pdf', bbox_inches="tight", pad_inches=0.05)
plt.close()
