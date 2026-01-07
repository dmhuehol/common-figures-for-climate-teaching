''' icao_profile
Plot ICAO vertical atmospheric profile.
'''
from ambiance import Atmosphere
import matplotlib.pyplot as plt
import numpy as np

#  Heights in m
heights = np.linspace(5e3, 35e3, num=1000)
atmos = Atmosphere(heights)
heights_km = heights / 1000
temperatures = atmos.temperature_in_celsius

plt.rcParams.update({'font.family': 'Figtree'})
#  'font.weight': normal, bold, heavy, light, ultrabold, ultralight
plt.rcParams.update({'font.weight': 'normal'})
plt.rcParams.update({'font.size': 12})
fig = plt.figure()
ax = fig.add_subplot(111)
ax.spines[['right', 'top']].set_visible(False)
plt.plot(temperatures, heights_km, color='#bb32a1', lw=2)
# plt.title(
#     'International Civil Aviation Organization Standard Atmosphere',
#     fontsize=12)
plt.ylim([5, 35])
plt.ylabel('Height (km)', fontweight='bold')
plt.xlim([-60, 0])
plt.xlabel('Temperature (˚C)', fontweight='bold')
plt.savefig('icao_temp_profilestrat.pdf')
