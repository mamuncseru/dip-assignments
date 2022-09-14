import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

def histogram(img, bins, min_val, max_val):
    dx = (max_val - min_val) / bins
    x = np.zeros(bins)
    y = np.zeros(bins+1)

    for i in range(bins):
        x[i] = i*dx + min_val

    for v in img:
        bin = int((v - min_val) / dx)
        y[bin] += 1

    y[bins -2] += y[bins - 1]
    y = y[:bins]

    plt.bar(x, y, width=dx)




def main():
    # reading an image
    rgb = cv.imread('angrybird.png')
    color = ('b','g','r')
    
    # separting the color channels
    red = rgb[:, :, 0]
    green = rgb[:, :, 1]
    blue = rgb[:, :, 2]


    #converting to grayscale 
    grayscale = cv.cvtColor(rgb, cv.COLOR_RGB2GRAY)

    # converting to binary
    _, binary = cv.threshold(grayscale, 50, 255, cv.THRESH_BINARY)
    


        
    plt.figure(figsize=(15, 15))

    # plotting histogram 
    plt.subplot(3, 2, 1)
    histr = cv.calcHist([red], [0],None,[256],[0,256])
    plt.plot(histr)

    plt.title('histogram by open-cv')
    plt.subplot(3, 2, 2)
    histogram(red.ravel(), 256, 0, 256)
    plt.title('Manually created histogram')
    plt.subplot(3, 2, 3)
    plt.hist(red.ravel(), 256, [0, 256])
    plt.title('histogram by matplotlib.pyplot')
    plt.subplot(3, 2, 4)
    counts, bins = np.histogram(red, range(257))
    # plot histogram centered on values 0..255
    plt.bar(bins[:-1] - 0.5, counts, width=1, edgecolor='none')
    plt.xlim([-0.5, 255.5])
    plt.title('histogram by numpy')
    plt.savefig('manual_histogram.png')

# calling the main function
if __name__ == '__main__':
    main()
