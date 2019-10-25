# This is to import the modules required for this module of code
from PIL import Image
import image_slicer
import multiprocessing
from abcd import Steganography
import math


# Generate the names of the image slices from the tuple returned by image_slicer
def imageName(image_slices):
	names=[]
	for i in image_slices:
		a=str(i).split('-')
		b=a[1][1:len(a[1])-1]
		names.append(b)
	return names

# This is to break the image into multiple slices
def sliceImage(image,number):
	image_pieces=image_slicer.slice(name, number)
	return image_pieces

# This module of code is used to split the string into n eq parts
def message_split(message,number):
	n=math.ceil(len(message)/number)
	ms=[]
	for i in range(number):
		if ((i+1)*n) < len(message) : 
			ms.append(message[i*n:(i+1)*n])
		else:
			ms.append(message[i*n:])
	return ms	

# Taking the name of the steg image from the user
name=input("Enter the name of the image:")
# Taking the message from the user
number=int(input("Enter the number of slice:"))
# Slicing the image
image_slices=sliceImage(name,number)
# Taking the message input
complete_message=input("Enter the message to hide:")
# Slicing the message
message=message_split(complete_message,number)
print("The split message is:",message)

# Calling the Steganography module from all the image pieces
nameImage=imageName(image_slices)
for i in range(len(nameImage)):
	Steganography(nameImage[i],message[i],i)

