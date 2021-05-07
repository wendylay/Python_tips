import netCDF4 as nc
import numpy as np
f_w = nc.Dataset('Y_distribution.nc', 'w', format='NETCDF4')


# define dimensions
longs = f_w.createDimension('longitude', size=len(lon))
lats = f_w.createDimension('latitude', size=len(lat))

# create variables
lat_w = f_w.createVariable('lat', np.float32, 'latitude')
lon_w = f_w.createVariable('lon', np.float32, 'longitude')
output_w = f_w.createVariable('2d_data', np.float32, ('latitude', 'longitude'))

# lon/lat/output are np.array, 1d, 1d, 2d
lon_w[:] = lon
lat_w[:] = lat
output_w[:] = output
f_w.close()

