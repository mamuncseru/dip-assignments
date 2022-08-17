import numpy as np
import matplotlib.pyplot as plt

def main():
	img_path = 'village.jpeg'
	rgb_img = plt.imread(img_path)
	
	# transformation constants
	T1 = 135	# threshold 1
	T2 = 220	# threshold 2
	c = 10
	p = 5
	epsilon = 0.0000001
	
	# 1st transformation
	trans1_img = rgb_img.copy()
	valid_indices = np.logical_and(trans1_img>=T1, trans1_img<=T2)
	trans1_img[valid_indices] = 100
	trans1_img[trans1_img != 100] = 10
	trans1_img.dtype = np.uint8
	
	# 2nd transformation
	trans2_img = rgb_img.copy()
	valid_indices = np.logical_and(trans2_img>=T1, trans2_img<=T2)
	trans2_img[valid_indices] = 100
	trans2_img.dtype = np.uint8
	
	# 3rd transformation
	trans3_img = rgb_img.copy()
	trans3_img = np.uint8(np.log(2+trans3_img) * c)

	
	# 4rth transformation
	trans4_img = rgb_img.copy()
	trans4_img = np.uint8(c * np.power((trans4_img + epsilon), p))

	
	print(trans4_img.min())
	
	#trans4_img.dtype = np.uint8
	
	images = [rgb_img, trans1_img, trans2_img, trans3_img, trans4_img]
	titles = ['RGB', 'Transformation 1', 'Transformation 2', 'Transformation 3', 'Transformation 4']
	
	for img in images:
		print(img.shape)
		
	fig, axs = plt.subplots(2, 3, figsize=(14, 8))
	
	for i, ax in enumerate(axs.flatten()[:len(images)]):
		ax.imshow(images[i])
		ax.set_title(titles[i])
	
	plt.show()
	
if __name__ == "__main__":
	main()
	
	
	 
