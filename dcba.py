# This module of code is used as a middleware to decrypt the messages
# Importing all the required packages
from PIL import Image
from numpy import array
from cryptography.fernet import Fernet
from Population import Population
from Chromosome import Chromosome
from Fitness import Fitness
from GA import GA
from Pit import Pit
from visual_decrypt import visual_decrypt
import time


class dcba:
	def __init__(self,number):

		# Creating the pixel index table from the pit file
		file=open('pit1'+str(number)+'.csv','r')
		a=file.readlines()
		cipherLen=len(a)
		pitTable=[]
		for i in range(cipherLen):
		    pitTable.append(Pit())
		xValue=0
		yValue=0
		diff=[None]*3
		index=0
		for i in a:
		    t=i.split(',')
		    xValue=int(t[0])
		    yValue=int(t[1])
		    diff[0]=int(t[2])
		    diff[1]=int(t[3])
		    string=t[4]
		    string=string[:len(string)-1]
		    diff[2]=int(string)
		    pitTable[index]=Pit(xValue,yValue,diff)
		    index+=1
		print("PIT table generated")


		# Starting the visual decrypting of the image
		print("Visual decryption algorithm started")
		objVisual=visual_decrypt()
		imageName=objVisual.decrypt()
		print('The visual cryptography algorithm has completed it\'s execution')



		# Extracting the hidden secret in the image
		img=Image.open(imageName)
		arr1=array(img)
		height=len(arr1)  # The number of rows in the image
		width=len(arr1[0])   # The number of columns in the image
		dcipherBytes=[None]*len(pitTable)
		dcipherIndex=0
		count=0
		poi=0
		toi=0