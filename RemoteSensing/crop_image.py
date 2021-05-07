import netCDF4 as nc
import numpy as np

dataset = nc.Dataset('E:/oisst-avhrr-v02r01.19970101.nc')

lat_set = np.array(dataset.variables['lat'][:])  # 1d
lon_set = np.array(dataset.variables['lon'][:])  # 1d
sst = np.array(dataset.variables['sst'][:])  # 2d
sst = sst[0, 0, :, :]
# find the row and col
row = np.where((lat_set > -75) & (lat_set < -70))[0]
col = np.where((lon_set > 167) & (lon_set < 177))[0]

# subset of 2d data
lon = lon_set[col]
lat = lat_set[row]
sst = sst[row][:, col]  # crop 2d data
