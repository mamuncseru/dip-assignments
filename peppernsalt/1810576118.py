import matplotlib.pyplot as plt
import cv2
import numpy as np
import random

def sp_noise(image, prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = image.copy()
    if len(image.shape) == 2:
        black = 0
        white = 255            
    else:
        colorspace = image.shape[2]
        if colorspace == 3:  # RGB
            black = np.array([0, 0, 0], dtype='uint8')
            white = np.array([255, 255, 255], dtype='uint8')
        else:  # RGBA
            black = np.array([0, 0, 0, 255], dtype='uint8')
            white = np.array([255, 255, 255, 255], dtype='uint8')
    probs = np.random.random(output.shape[:2])
    output[probs < (prob / 2)] = black
    output[probs > 1 - (prob / 2)] = white
    return output

def median_filter(data, filter_size):
    temp = []
    indexer = filter_size // 2
    data_final = []
    data_final = np.zeros((len(data),len(data[0])))
    for i in range(len(data)):

        for j in range(len(data[0])):

            for z in range(filter_size):
                if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                    for c in range(filter_size):
                        temp.append(0)
                else:
                    if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                        temp.append(0)
                    else:
                        for k in range(filter_size):
                            temp.append(data[i + z - indexer][j + k - indexer])

            temp.sort()
            data_final[i][j] = temp[len(temp) // 2]
            temp = []
    return data_final

def main():
	'''	Load an RGB image.	'''
	img_path = 'angrybird.png'
	grayscale = cv2.imread(img_path, 0)

		
	'''	Convert the RGB image into grayscale and binary image.	'''
	# grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
	noise_img = sp_noise(grayscale, 0.05)
	

	gaussian_kernel = np.ones((3, 3), dtype=np.float32)/25
	gauss_img = cv2.filter2D(noise_img, -1, gaussian_kernel)

	med_img = median_filter(noise_img, 3)


	plt.figure(figsize=(12, 12))
	plt.subplot(2, 2, 1)
	plt.title('grayscale')
	plt.imshow(grayscale, cmap='gray')
	plt.subplot(2, 2, 2)
	plt.title('noise')
	plt.imshow(noise_img, cmap='gray')
	plt.subplot(2, 2, 3)
	plt.title('gaussian')
	plt.imshow(gauss_img, cmap='gray')
	plt.subplot(2, 2, 4)
	plt.title('median')
	plt.imshow(med_img, cmap='gray')

	plt.savefig('noise.jpg')



	
if __name__ == '__main__':
	main()
