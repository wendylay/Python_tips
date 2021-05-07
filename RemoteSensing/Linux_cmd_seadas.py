import os
import re

'''
Batch process L1 with Seadas in Linux
2021.4.19
'''

# curdir = os.getcwd()
curdir = './'
filelist = os.listdir(path=curdir)

for file in filelist:
    if os.path.isdir(os.path.join(curdir, file)):
        file_path = os.path.join(curdir, file)

        ifile = os.path.join(file_path,
                             list(filter(lambda x: re.match(r'.*MTL.txt', x), os.listdir(path=file_path)))[0])
        ofile = os.path.join(curdir, file[10:25] + '.L2_LAC_OC')
        # l2prod is the output value
        command_line = 'l2gen ifile={} ofile={} suite="OC" l2prod="Rrs, Rrs_nnn, cloud_albedo"'.format(ifile, ofile)
        os.system(command_line)
