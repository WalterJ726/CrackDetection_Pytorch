
import os
import re
import sys

# fileList = os.listdir(r"E:\正课\大二上\计算机网络\网络编程\图像去噪声\dice")
fileList = os.listdir(r"/CrackDetection/data/dice")
# 输出此文件夹中包含的文件名称
# print("修改前：" + str(fileList)[1])
# 得到进程当前工作目录
currentpath = os.getcwd()
# 将当前工作目录修改为待修改文件夹的位置
os.chdir(r"/CrackDetection/data/dice")
# 名称变量
num = 0
# 遍历文件夹中所有文件
for fileName in fileList:
    # 匹配文件名正则表达式
    # pat = ".+\.(json)"
    # 进行匹配
    # pattern = re.findall(pat, fileName)
    # 文件重新命名
    newname = str(num) + '.jpg'
    os.rename(fileName, newname)
    # 改变编号，继续下一项
    num = num + 1
# print("***************************************")
# 改回程序运行前的工作目录
os.chdir(currentpath)
# 刷新
sys.stdin.flush()
# 输出修改后文件夹中包含的文件名称
# print("修改后：" + str(os.listdir(r"./neteasy_playlist_data3"))[1])