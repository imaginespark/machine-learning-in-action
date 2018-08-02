# -*- coding: utf-8 -*-
"""

@author: Jerry
"""

import numpy as np
import matplotlib.pyplot as plt
import KMeans

# 将经纬度转换为距离    
def distSLC(vecA, vecB):#Spherical Law of Cosines  #
    a = np.sin(vecA[0,1]*np.pi/180) * np.sin(vecB[0,1]*np.pi/180)
    b = np.cos(vecA[0,1]*np.pi/180) * np.cos(vecB[0,1]*np.pi/180) * np.cos(np.pi * (vecB[0,0]-vecA[0,0]) /180)
    
    return np.arccos(a + b)*6371.0  

def clusterClubs(numClust=5):
    datList = []
    for line in open('places.txt').readlines():#获取地图数据
        lineArr = line.split('\t')
        datList.append([float(lineArr[4]), float(lineArr[3])])#逐个获取第四列和第五列的经纬度信息
    datMat = np.mat(datList)
    myCentroids, clustAssing = KMeans.biKmeans(datMat, numClust, distMeas=distSLC)
    
    fig = plt.figure()
    rect=[0.1,0.1,0.8,0.8]#创建矩形
    #创建不同标记图案
    scatterMarkers=['s', 'o', '^', '8', 'p', 'd', 'v', 'h', '>', '<']
    axprops = dict(xticks=[], yticks=[])
    
    ax0=fig.add_axes(rect, label='ax0', **axprops)
    imgP = plt.imread('Portland.png')#导入地图
    ax0.imshow(imgP)
    ax1=fig.add_axes(rect, label='ax1', frameon=False)
    for i in range(numClust):
        ptsInCurrCluster = datMat[np.nonzero(clustAssing[:,0].A==i)[0],:]
        markerStyle = scatterMarkers[i % len(scatterMarkers)]
        ax1.scatter(ptsInCurrCluster[:,0].flatten().A[0], ptsInCurrCluster[:,1].flatten().A[0], marker=markerStyle, s=90)
    ax1.scatter(myCentroids[:,0].flatten().A[0], myCentroids[:,1].flatten().A[0], marker='+', s=300)
    plt.show()
    
if __name__ == '__main__': 
    clusterClubs(5)