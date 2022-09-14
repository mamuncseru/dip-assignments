import numpy as np
import matplotlib.pyplot as plt
import cv2

def main():
	img_path = 'village.jpeg'
	bgr_img = cv2.imread(img_path)
	gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
	
	generate_10_random_filter = [np.random.randint(0,2, 9).reshape(3,3) for i in range(10)]
	
	
	# filter visualizing
	'''
	for i in range(10):
		print(generate_10_random_filter[i])
		
	fig, axs = plt.subplots(2, 5, figsize=(14, 6))
	
	for i, ax in enumerate(axs.flatten()):
		ax.imshow(generate_10_random_filter[i])
		ax.set_title('filter %i'%i)
		
	plt.show()
	'''
	filtered_imgs = []
	for i in range(10):
		filtered_imgs.append(cv2.filter2D(src=gray_img, ddepth=-1, kernel=generate_10_random_filter[i]))
	
	fig, axs = plt.subplots(4, 5, figsize=(20, 12))
	
	for i, ax in enumerate(axs.flatten()[:10]):
		ax.imshow(filtered_imgs[i], cmap='gray')
		ax.set_title('filter %i'%i)
		
	for i, ax in enumerate(axs.flatten()[10:]):
		ax.imshow(generate_10_random_filter[i], cmap='gray')
		ax.set_title('filter %i'%(i))
		
	plt.show()
		
	plt.show()
	
	
	
	
if __name__ == "__main__":
	main()
