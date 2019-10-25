# This module is used to handle operations related to visual decryption
from PIL import Image
from numpy import array
import numpy as np
from cryptography.fernet import Fernet

class visual_decrypt:
	def __init__(self,number):
		self.number=number

	def decrypt(self):
		# Now let's start the pixel extraction phase of the project
		#First we'll extract the red pixel values
		file_red=open('red_pixel'+str(self.number),'r')
		red=file_red.readline()
		print("Finished extracting the red pixel values")
		rc=file_red.readline()
		file_red.close()

		#  Now let's extract the green pixel values
		file_green=open('green_pixel'+str(self.number),'r')
		green=file_green.readline()
		print("Finished extracting the green pixel values")
		file_green.close()

		# Now let's extract the blue pixel values
		file_blue=open('blue_pixel'+str(self.number),'r')
		blue=file_blue.readline()
		print("Finished extracting the blue pixel values")
		file_blue.close()

		#Now we need to start the decryption phase of this module
		key=input("Enter the key of the encryption: ")
		key=key.encode('utf-8')
		cipher_suite=Fernet(key)
		# Decrypting the red pixels
		red_decrypt=cipher_suite.decrypt(red.encode('utf-8'))
		rc_decrypt=cipher_suite.decrypt(rc.encode('utf-8'))
		print("Successfully decrypted the red pixels")
		

		# Decrypting the green pixels
		green_decrypt=cipher_suite.decrypt(green.encode('utf-8'))
		print("Successfully decrypted the green pixels")
		
		# Decrypting the blue pixels
		blue_decrypt=cipher_suite.decrypt(blue.encode('utf-8'))
		print("Successfully decrypted the blue pixels")
		
		# Now we have completed the decrypting phase of this module

		#Testing part
		red_decrypt=red_decrypt.decode('utf-8')
		green_decrypt=green_decrypt.decode('utf-8')
		blue_decrypt=blue_decrypt.decode('utf-8')
		print("The length of the red strign is:",len(red_decrypt))
		print("The length of the green strign is:",len(green_decrypt))
		print("The length of the  vlue strign is:",len(blue_decrypt))




		#Now we convert the extracted string of pixels into a list
		# We convert the red pixel first
		red_list=(red_decrypt.split(","))
		
		#Now we convert the green pixels
		green_list=(green_decrypt).split(",")
		
		# Now we convert the blue pixels
		blue_list=(blue_decrypt).split(",")
		
		#Now we are done with the list creation phase of this module

		#Finding the number of rows and columns 
		
		rc_decrypt=rc_decrypt.decode('utf-8')
		rc_list=str(rc_decrypt).split(',')
		row=int(rc_list[0])
		column=int(rc_list[1])
		
		# Now we need to start the image matrix building phase of this module
		rows_val=[]
		count=0
		test_c=0
		columns_val=[]
		while count<(row*column):
			if len(columns_val)==column:
				test_c=test_c+1
				rows_val.append(columns_val)
				columns_val=[]
			pixel_val=[]
			pixel_val.append(int(red_list[count]))
			pixel_val.append(int(green_list[count]))
			pixel_val.append(int(blue_list[count]))
			columns_val.append(pixel_val)
			count=count+1
		rows_val.append(columns_val)

		print("The process of building the image is complete...")
		#Now we are done with creating the matrix 

		# Now we have make an image from the image
		rows_val=array(rows_val)
		#print(rows_val)
		final_image=Image.fromarray(rows_val.astype('uint8'))
		final_image.save('final_crypt'+str(self.number)+'.png')
		print("The image has been created and saved in the project folder")
		print("The name of the image file is final_crypt.png")
		print("The number of rows in the image is:",row)
		print("The numbe of columns in the image is:",column)
		print("The value of the count is:",count)
		#print("The value of test_c is:",test_c)
		for i in range(0,row):
			rows_val[i][0][0]
		# Returning the name of the final image built from the pieces
		return 'final_crypt'+str(self.number)+'.png'
