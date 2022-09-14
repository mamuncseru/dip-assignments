import cv2
import matplotlib.pyplot as plt
import numpy as np
def main():
    # reading an image
    rgb = cv2.imread('angrybird.png')


    #converting to grayscale 
    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)


    sobel_kernel = np.array([[1, 0, -1],
                            [2, 0, -2],
                            [1, 0, -1]])
    
    laplacian_kernel = np.array([[0, -1, 0],
                                [-1, 4, -1],
                                [0, -1, 0]])
    
    sobel_img = cv2.filter2D(src=grayscale, ddepth=-1, kernel=sobel_kernel)
    laplacian_img = cv2.filter2D(src=grayscale, ddepth=-1, kernel=laplacian_kernel)
    
    plt.figure(figsize=(10, 12))
    
    plt.subplot(1, 3, 1)
    plt.title('original grayscale')
    plt.imshow(grayscale, cmap='gray')
    
    plt.subplot(1, 3, 2)
    plt.title('Sobel kernel')
    plt.imshow(sobel_img, cmap='gray')    
    
    plt.subplot(1, 3, 3)
    plt.title('Laplacian kernel')
    plt.imshow(laplacian_img, cmap='gray')
    plt.savefig('filtering.jpg')

# calling the main function
if __name__ == '__main__':
    main()
