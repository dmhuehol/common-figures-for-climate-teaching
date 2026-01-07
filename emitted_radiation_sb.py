''' Plot emitted radiation for range of temperatures following
Stefan-Boltzmann Law.
'''
import os
import sys

from icecream import ic
from matplotlib import font_manager as fm
import matplotlib.pyplot as plt
import numpy as np

from fun_helper import stefan_boltzmann as sb

font_path_local = '/Users/danielhueholt/Library/Fonts/'
if os.path.exists(font_path_local):
    for font in fm.findSystemFonts(font_path_local):
        fm.fontManager.addfont(font)

temperatures = np.arange(180, 6000, 1)
rad_wm2 = sb(temperatures)
emphasis_temp = np.array([184, 288, 330, 5772])
emphasis_rad_wm2 = sb(emphasis_temp)

plt.rcParams.update({'font.family': 'Figtree'})
#  'font.weight': normal, bold, heavy, light, ultrabold, ultralight
plt.rcParams.update({'font.weight': 'normal'})
plt.rcParams.update({'font.size': 12})
fig = plt.figure()
ax = fig.add_subplot(111)
ax.spines[['right', 'top']].set_visible(False)
plt.plot(temperatures, rad_wm2, color='#69e9d9', lw=4)
plt.scatter(emphasis_temp[:-1], emphasis_rad_wm2[:-1], color='#7942bb', s=140)
plt.scatter(emphasis_temp[-1], emphasis_rad_wm2[-1], color='#ff33ec', s=140)
plt.ylabel('Radiation per unit area (W/m2)', fontweight='bold')
plt.xlabel('Temperature (K)', fontweight='bold')
plt.savefig('emitted-radiation_EarthRangeSun.pdf')
