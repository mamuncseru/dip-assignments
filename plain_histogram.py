# import libraries
import cv2
import matplotlib.pyplot as plt

def main():
	
	# read an image with cv2
	img_path = 'village.jpeg'
	bgr_img = cv2.imread(img_path)
	
	# convert to rgb
	rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)
	
	# convert to gray
	gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY)
	
	# convert to binary
	_, bin_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
	
	
	# calculate histogram for every image
	
	# rgb we need to calculate for every channel
	
	red_hist = cv2.calcHist(images=[rgb_img], channels=[0], mask=None, histSize=[255], ranges=[0,255]) 
	green_hist = cv2.calcHist(images=[rgb_img], channels=[1], mask=None, histSize=[255], ranges=[0, 255])
	blue_hist = cv2.calcHist(images=[rgb_img], channels=[2], mask=None, histSize=[255], ranges=[0, 255])
	
	# grayscale hist image
	gray_hist = cv2.calcHist(images=[gray_img], channels=[0], mask=None, histSize=[255], ranges=[0, 255])
	
	# binary hist image
	binary_hist = cv2.calcHist(images=[bin_img], channels=[0], mask=None, histSize=[255], ranges=[0, 255])
	
	
	hist_plots = [red_hist, green_hist, blue_hist, gray_hist, binary_hist]
	hist_titles = ['red channel', 'green channel', 'blue channel', 'gray', 'binary']
	
	images = [rgb_img, gray_img, bin_img]
	titles = ['RGB', 'Grayscale', 'Binary']
	
	fig, axs = plt.subplots(1, 5, figsize=(12, 4))
	
	for i, ax in enumerate(axs.flatten()):
		ax.plot(hist_plots[i])
		ax.set_title(hist_titles[i])
		
	plt.show()
	
	"""
	for i in range(3):
		ax[i].imshow(images[i], cmap=['gray', 'viridis'][len(images[i].shape) == 3])
		ax[i].set_title(titles[i])
	
	plt.show()
	"""
if __name__ == "__main__":
	main()
