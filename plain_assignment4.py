import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram(img):
	hist_arr = np.zeros((256))
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			hist_arr[img[i,j]] += 1
			

	plt.plot(hist_arr)
	plt.xlim([0,255])
	plt.show()



def main():
	img_path = 'village.jpeg'
	
	bgr_img = cv2.imread(img_path)
	
	histogram(bgr_img[:, :, 0])
	
	blue_hist = cv2.calcHist([bgr_img], [0], None, [255], [0,255])
	
	plt.plot(blue_hist)
	plt.show()
	
	
	
	



if __name__ == '__main__':
	main()
