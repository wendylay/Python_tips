import numpy as np
import netCDF4 as nc
import pandas as pd

# Modis data file
filename = 'E:/A2014313000000.L2_LAC_OC.nc'
data = nc.Dataset(filename)
chl = np.array(data.groups['geophysical_data']['chlor_a'])

lon = np.array(data.groups['navigation_data']['longitude'])
lat = np.array(data.groups['navigation_data']['latitude'])

# select roi
chl_sel = chl[(lon > -160) & (lon < -150) & ((lat > -64) & (lat < -60))]

chl_sel[chl_sel == -32767] = np.nan
chl_sel = chl_sel[~np.isnan(chl_sel)]
