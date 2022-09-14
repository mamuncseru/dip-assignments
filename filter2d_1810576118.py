'''	
	------------------
	Neighborhood processing.
	------------------
	Sangeeta Biswas
	Associate Professor
	Dept. of Computer Science & Engineering
	University of Rajshahi
	Rajshahi, Bangladesh
	
	7.6.2022
'''

import matplotlib.pyplot as plt
import cv2
import numpy as np

def filter2d(image, kernel):

	''' assume it's 3 x 3 kernel'''

	height,width,channel=image.shape
	result=np.zeros(image.shape,dtype=np.float32)
	for j in range(1,height-1):
		for i in range(1,width-1):
			for a in range(channel):
				result[j,i,a]=(
					(
					kernel[0]*image[j-1,i-1,a] + 
					kernel[1]*image[j-1,i,a] + 
					kernel[2]*image[j-1,i+1,a] + 
					kernel[3]*image[j,i-1,a] + 
					kernel[4]*image[j,i,a] + 
					kernel[5]*image[j,i+1,a] + 
					kernel[6]*image[j+1,i-1,a] + 
					kernel[7]*image[j+1,i,a] + 
					kernel[8]*image[j+1,i+1,a]
					)
				)
	return result

def main():
	'''	Load an RGB image.	'''
	img_path = 'angrybird.png'
	rgb = plt.imread(img_path)
	print(rgb.shape)
		
	'''	Convert the RGB image into grayscale and binary image.	'''
	grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
	print(grayscale.shape)
	
	'''	Prepare kernels/filters/masks.	'''
	kernel1 = np.ones((3, 3), dtype = np.float32) * 2 / 9
	print('Kernel1: {}'.format(kernel1))	
	kernel2 = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
	print('Kernel2: {}'.format(kernel2))
	
	'''	Neighborhood processing. '''
	processed_img2 = cv2.filter2D(rgb, -1, kernel2)
	processed_img3 = filter2d(rgb, kernel2.ravel())
		
	'''	Plot images. '''
	img_set = [rgb, processed_img2, processed_img3]
	title_set = ['RGB', 'Kernel2', 'kernel2_man']
	plot_img(img_set, title_set)

def plot_img(img_set, title_set):
	n = len(img_set)
	plt.figure(figsize = (20, 20))
	for i in range(n):
		img = img_set[i]
		ch = len(img.shape)
	
		plt.subplot(2, 3, i + 1)
		if (ch == 3):
			plt.imshow(img_set[i])
		else:
			plt.imshow(img_set[i], cmap = 'gray')
		plt.title(title_set[i])
	plt.savefig('man_filter2d.png')		
	
if __name__ == '__main__':
	main()
