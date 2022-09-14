import cv2
import matplotlib.pyplot as plt
import numpy as np
def main():
    # reading an image
    rgb = cv2.imread('angrybird.png')


    #converting to grayscale 
    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)


    mask = np.zeros(grayscale.shape, dtype="uint8")
    
    mask = cv2.circle(mask, (245, 300), 200, 255, -1)
    
    masked = cv2.bitwise_and(grayscale, mask, mask=mask)
    
    plt.figure(figsize=(10, 12))
    
    plt.subplot(1, 2, 1)
    plt.title('Before masked')
    plt.imshow(grayscale, cmap='gray')    
    
    plt.subplot(1, 2, 2)
    plt.title('after masked')
    plt.imshow(masked, cmap='gray')
    plt.savefig('masked.jpg')

# calling the main function
if __name__ == '__main__':
    main()
