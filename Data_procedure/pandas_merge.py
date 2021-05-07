import numpy as np
import pandas as pd
import scipy.io as sio

file_dir = 'D:/others/20200829-depth/model establish final/'
loc = pd.read_excel(file_dir + 'Training_database_0525.xlsx', sheet_name='location')
sat_mat = 'D:/0525_rho.mat'
data = sio.loadmat(sat_mat)

df_sat = pd.DataFrame(data['save_matrix'],
                      columns=['lat', 'lon', 'rhot443', 'rhot482', 'rhot561', 'rhot655', 'rhot865', 'rhot1609',
                               'rhot2201'], index=None)
k = pd.merge(loc, df_sat, how='inner', on=['lat', 'lon'])
print(k)

# if the pandas value y index is random,
# before 'df1.merge', you should
# y = y.reset_index()
# y.reset_index(drop=True, inplace=True)