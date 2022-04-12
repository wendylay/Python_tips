"""
Process Landsat8 image from L1 to L2 by ACOLITE in batch
refer: https://blog.csdn.net/mrzhy1/article/details/108543824

"""
import os
from subprocess import check_call

def save_setting_file():
    # 需要修改的变量
    example = 'E:/Landsat 8/acolite_python_settings.txt'  # 一个Setting文件例子
    # 注意setting文件的第91行为输入文件路径(从0开始)
    # 第92行为输出文件的路径。运行之前应该先检查,不是的话根据实际情况修改
    s2dir = 'E:/Bahamas_large_depth/raw/'  # 原始数据的存放目录,注意加上最后的/
    resultDir = 'E:/Bahamas_large_depth/raw/'  # Acolite大气校正后结果的存放路径。注意加上最后的/

    # 读出例子Setting文件的内容
    with open(example, 'r') as ef:
        examplecon = ef.read().split('\n')[:-1]

    s2fileList = os.listdir(s2dir)
    settingList = []  # 存放各setting文件的路径

    # make setting file
    for s2f in s2fileList:
        if not (os.path.isdir(os.path.join(s2dir, s2f))):
            continue
        inputfile = s2dir + s2f

        outputfile = resultDir + s2f
        os.makedirs(outputfile, exist_ok=True)

        examplecon[110] = 'inputfile=' + inputfile
        examplecon[111] = 'output=' + outputfile
        settingFile = resultDir + s2f + '_setting.txt'
        settingList.append(settingFile)

        with open(settingFile, 'w') as outsetting:
            for ec in examplecon:
                outsetting.write(ec + '\n')


def run_setting_file():
    # run setting file with cmdline
    acolitepath = 'D:/software/acolite/launch_acolite.py'  # acolite的路径
    setting_file_path = 'E:/Bahamas_large_depth/raw/'
    settingList = os.listdir(setting_file_path)
    for stl in settingList:
        if '_setting' in stl:
            cmdline = 'python ' + acolitepath + ' --cli --settings=' + '"' + setting_file_path + stl + '"'
            check_call(cmdline)


if __name__ == '__main__':
    save_setting_file()
    run_setting_file()
