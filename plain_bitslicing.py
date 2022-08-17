# import libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np

# main function
def main():
	
	img_path = 'village.jpeg'
	
	rgb_img = plt.imread(img_path)
	
	gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY)
	
	pixel_list = []
	
	for i in range(gray_img.shape[0]):
		for j in range(gray_img.shape[1]):
			pixel_list.append(np.binary_repr(gray_img[i, j], width=8))
			
	
	slice_img = []
	slice_titles = ['eight', 'seven', 'six', 'five', 'four', 'three', 'two', 'one']
		
	for i in range(8):		
		slice_img.append((np.array([int(pixel_binary[i]) for pixel_binary in pixel_list])*(2**(7-i))).reshape(gray_img.shape))
		
	fig, axs = plt.subplots(2, 4, figsize=(14, 8))
	for i, ax in enumerate(axs.flatten()):
		ax.imshow(slice_img[i], cmap='gray')
		ax.set_title(slice_titles[i])
		
	plt.show()
	
if __name__ == "__main__":
	main()






		
	
