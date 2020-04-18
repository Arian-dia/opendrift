"""
3D
=============
"""
#!/usr/bin/env python

from opendrift.readers import reader_ECOM_building
from opendrift.models.oceandrift3D import OceanDrift3D

o = OceanDrift3D(loglevel=0)  # Set loglevel to 0 for debug information

reader_pcse = reader_ECOM_building.Reader('/home/arian/IC/arquivos_cdf/z_six_days.nc')

o.add_reader([reader_pcse])

		# Seeding some particles
lon = -45.1; lat = -24;

time = reader_pcse.start_time
# Seed elements at defined position and time
import numpy as np

o.seed_elements(lon, lat, z= -45, radius=6, number=200, time=time)


# Adjusting some configuration
#o.set_config('drift:current_uncertainty', .1)
o.set_config('drift:wind_uncertainty', 2)
o.set_config('processes:verticaladvection', True)

# Running model (until end of driver data)
#o.run(duration=timedelta(hours=24))
o.run(steps=66*2, time_step=1800)  
#o.run(duration=timedelta(hours=24))


# Print and plot results
print(o)
o.plot(fast = True)  # Color lines according to depth
o.plot_property('z')

o.animation(filename='3D_ecom.gif')


