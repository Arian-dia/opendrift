#!/usr/bin/env python

import numpy as np

from elements import LagrangianArray
from elements.passivetracer import PassiveTracer
from elements.oil import Oil
from elements.larvae import Larvae, CodLarvae, HalibutLarvae

#print '####################################'
#print LagrangianArray.parameters
#print '####################################'
#print Oil.parameters
#print '####################################'
#print Larvae.parameters
#print '####################################'
#print CodLarvae.parameters
#print '####################################'
#print HalibutLarvae.parameters
#print '####################################'

lons = np.array([32, 3, 8])
lats = np.array([22, 3, 4])

#o = LagrangianArray(lon=lons, lat=lats)
#o = PassiveTracer(lon=lons, lat=lats)
o = Oil(lon=lons, lat=lats, depth=44, massOil=[100])
#o = CodLarvae(lon=lons, lat=lats, CodLarvaeProperty1=[1], length=10)
#o = HalibutLarvae(lon=lons, lat=lats, HalibutLarvaeProperty1=[2], length=10)
#
#print '####################################'
o.show_data()
o.update_properties()
o.update_position()
print '####################################'
o.show_data()
#print '####################################'
#
#c = CodLarvae(lon=[32, 3, 8], lat=[22, 3, 4], depth=[44], CodLarvaeProperty1=[5], length=[10])
#c.update_properties()
#print c
#print o.variables['depth']
