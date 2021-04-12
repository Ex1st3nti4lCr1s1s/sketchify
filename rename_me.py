from instabot import Bot
import sys, shutil
from PIL import Image
import cv2



def make_image():
	'''    in case you want to read names from a file, uncomment
	for x in f.readlines():
		name = str(x.strip())
		photo = name+".jpg"
		img = cv2.imread(photo)
		print(photo)
	'''
	photo = "cattliina.jpg" # change name
	img = cv2.imread(photo)
	gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

	inverted_gray_image = 255 - gray_image

	blurred_img = cv2.GaussianBlur(inverted_gray_image, (21,21),0) 

	inverted_blurred_img = 255 - blurred_img

	pencil_sketch_IMG = cv2.divide(gray_image, inverted_blurred_img, scale = 256.0)

		#Show the original image
	cv2.imshow('Original Image', img)
		#Show the new image pencil sketch
	cv2.imwrite("cattliina.png", pencil_sketch_IMG)
		#Display the window infinitely until any keypress
	cv2.waitKey(0)
	
def upload_process():
	shutil.rmtree("Config")

	bot = Bot()
	bot.login(username="", password="")

	file = open("names.txt", "r")
	for x in file.readlines():
		try:
			name = str(x.strip())
			photo = name + ".png"
			image = Image.open(photo)
			new_image = image.resize((720, 720 ))
			new_image.save(f'{name}.jpg')
			image_name = f'{name}.jpg'
			bot.upload_photo(photo=image_name, caption=f"@{name}")
		except:
			pass

	bot.logout()
	sys.exit()