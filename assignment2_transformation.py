from re import S
import cv2
from cv2 import log
import matplotlib.pyplot as plt
import numpy as np
import math

def main():
    rgbImg = plt.imread('RedEagle.jpg')
    grayscale = cv2.cvtColor(rgbImg,cv2.COLOR_RGB2GRAY)
    modified_Img1 = np.copy(grayscale)
    modified_Img2 = np.copy(grayscale)
    modified_Img3 = np.copy(grayscale)
    modified_Img4 = np.copy(grayscale)

    c = 17
    p = 71
    epsilon =  0.0000001
    T1 = 117
    T2 = 225


    for x in range(modified_Img1.shape[0]):
        for y in range(modified_Img1.shape[1]):
            r = modified_Img1[x,y]
            s_0 = 10
            s_1 = r
            if r >= T1 and r <= T2:
                s_0 = 100
                s_1 = 100
            s_2 = c*math.log(1+r)
            s_3 = c*pow((r+epsilon),p)
            
            modified_Img1[x,y] = s_0
            modified_Img2[x,y] = s_1
            modified_Img3[x,y] = s_2
            modified_Img4[x,y] = s_3

    img_set =  [grayscale, modified_Img1,modified_Img2,modified_Img3,modified_Img4]
    title_set = ['RGB Img','Gray Scale Img','Processed Img1','Processed Img2','Processed Img3','Processed Img4']
    plot_img(img_set,title_set)

def plot_img(img_set,title_set):
    plt.figure(figsize=(20,20))
    for i in range(len(img_set)):
        plt.subplot(2,3,i+1)
        plt.title(title_set[i])
        plt.imshow(img_set[i],cmap='gray')
    plt.savefig('figure1.png')
    plt.show()

if __name__== '__main__':
    main()
