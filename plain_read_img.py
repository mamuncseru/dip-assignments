import cv2
import matplotlib.pyplot as plt

def main():
	img_path = 'village.jpeg'
	bgr_img = cv2.imread(img_path)
	rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)
	gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY)
	ret, bin_img = cv2.threshold(gray_img, 127, 255, type=cv2.THRESH_BINARY)
	
	image = [rgb_img, gray_img, bin_img]
	fig, ax = plt.subplots(1, 3, figsize=(12, 5))
	for i in range(3):
		ax[i].imshow(image[i], cmap=['gray', 'viridis'][len(image[i].shape) == 3])
	
	plt.show()
	
if __name__ == "__main__":
	main()
