import cv2
import os
import numpy as np


# fileList = os.listdir(r"E:\Pyproject\CrackDetection\data\test")
d = []
all = 0.0
for i in range(237):
    # s2 = cv2.imread("./CrackDetection/data/dice2" + str(i) + ".png", 0)  # 模板
    s2 = cv2.imread("E:/Pyproject/CrackDetection/data/dice2/" + str(i) + ".png", 0)  # 模板
    row, col = s2.shape[0], s2.shape[1]
    s1 = cv2.imread("E:/Pyproject/CrackDetection/data/dice/" + str(i) + "_res.jpg", 0)  # 读取配准后图像
    s = []
    for r in range(row):
        for c in range(col):
            if s1[r][c] == s2[r][c]:  # 计算图像像素交集
                s.append(s1[r][c])
    m1 = np.linalg.norm(s)
    m2 = np.linalg.norm(s1.flatten()) + np.linalg.norm(s2.flatten())
    percentage = 2 * m1 / m2
    d.append(percentage)
    msg = "这是第{}张图的dice系数".format(i) + str(2 * m1 / m2)
    all = all + percentage
    # print(2*m1/m2)
    print(msg)
# results = all / 237.0
results = all / 237.0
print(results)