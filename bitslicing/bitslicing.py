import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():

    img = cv2.imread('angrybird.png')
    
    grayscale = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    pixel_list = []
    for i in range(grayscale.shape[0]):
        for j in range(grayscale.shape[1]):
            pixel_list.append(np.binary_repr(grayscale[i][j], width=8))

        
    eight_bit = (np.array([int(i[0]) for i in pixel_list], dtype=np.uint8) * 128).reshape(grayscale.shape[0], grayscale.shape[1])
    seven_bit = (np.array([int(i[1]) for i in pixel_list], dtype=np.uint8) * 64).reshape(grayscale.shape[0], grayscale.shape[1])
    six_bit = (np.array([int(i[2]) for i in pixel_list], dtype=np.uint8) * 32).reshape(grayscale.shape[0], grayscale.shape[1])
    five_bit = (np.array([int(i[3]) for i in pixel_list], dtype=np.uint8) * 16).reshape(grayscale.shape[0], grayscale.shape[1])
    four_bit = (np.array([int(i[4]) for i in pixel_list], dtype=np.uint8) * 8).reshape(grayscale.shape[0], grayscale.shape[1])
    three_bit = (np.array([int(i[5]) for i in pixel_list], dtype=np.uint8) * 4).reshape(grayscale.shape[0], grayscale.shape[1])
    two_bit = (np.array([int(i[6]) for i in pixel_list], dtype=np.uint8) * 2).reshape(grayscale.shape[0], grayscale.shape[1])
    one_bit = (np.array([int(i[7]) for i in pixel_list], dtype=np.uint8) * 1).reshape(grayscale.shape[0], grayscale.shape[1])

    plt.figure(figsize=(12, 12))

    plt.subplot(3, 3, 1)
    plt.imshow(grayscale, cmap='gray')
    plt.title('grayscale')

    plt.subplot(3, 3, 2)
    plt.imshow(eight_bit, cmap='gray')
    plt.title('8th bit')
    
    plt.subplot(3, 3, 3)
    plt.imshow(seven_bit, cmap='gray')
    plt.title('7th bit')


    plt.subplot(3, 3, 4)
    plt.imshow(six_bit, cmap='gray')
    plt.title('6th bit')
    
    plt.subplot(3, 3, 5)
    plt.imshow(five_bit, cmap='gray')
    plt.title('5th bit')

    
    plt.subplot(3, 3, 6)
    plt.imshow(four_bit, cmap='gray')
    plt.title('4th bit')
    
    plt.subplot(3, 3, 7)
    plt.imshow(three_bit, cmap='gray')
    plt.title('3rd bit')

    
    plt.subplot(3, 3, 8)
    plt.imshow(two_bit, cmap='gray') 
    plt.title('2nd bit')
    
    plt.subplot(3, 3, 9)
    plt.imshow(one_bit, cmap="gray")
    plt.title('1st bit(LSB)')


    plt.savefig('bitslice.jpg')

    

if __name__ == '__main__':
    main()
