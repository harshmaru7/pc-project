# The main aim of this module is to make the Ga_Encry module of code a bit more modular
# Now how to make it modular?
# Parameter 1: Name of the image in which we need to hide the text
# Parameter 2: Text that has to be hidden in the image
# Parameter 3: This is the number that has to be passed to this module to uniquely identify the files created by this

# This is to import the modules required for this module 
from PIL import Image
from numpy import array
from cryptography.fernet import Fernet
from Population import Population
from Chromosome import Chromosome
from Fitness import Fitness
from GA import GA
from Pit import Pit
from visual_cryptography import visual_cryptography
import time


# This is a helper function
# This moduel is used to return which one among r,g,b have the least difference with the cipher 
def getMinDx(allGenes,solution):
	genes=allGenes
	minDX=abs(solution-genes[0])
	chosen=0
	for i in range(len(genes)):
	    if abs(solution-genes[i])<minDX:
	        minDX=abs(solution-genes[i])
	        chosen=i
	for i in range(len(genes)):
	    if chosen==i:
	        genes[i]=(solution-genes[i])
	    else:
	        genes[i]=-1000
	return genes  

class Steganography:
	def __init__(self,name,message,number):

		# Calling the encryption module for the message
		messageUtf=message.encode('utf-8')
		key = Fernet.generate_key()
		cipher_suite = Fernet(key)
		cipher_text = cipher_suite.encrypt(messageUtf)
		plain_text = cipher_suite.decrypt(cipher_text)
		print("The cipher text is:",cipher_text)
		data=cipher_text.decode('utf-8')
		data=data+'~'
		# Getting the ASCII value of the encrypted strings.
		# This will be hidden inside the image passed to this module
		cipher=[]
		for i in data:
			cipher.append(ord(i))
		qwerty=cipher[:]


		# Now it's the time to load the image 
		#Extract pixel
		img=Image.open(name)
		arr=array(img)
		row=len(arr)
		column=len(arr[0])
		print("Row:",row)
		print("Column:",column)
		#testing=row
		#testing1=column

		print("Initializing the initial population")
		chromosomes= [None]*(row*column)
		index=0
		#Initialise chromosomes with pixel values
		for x in range(column):
			for y in range(row): 
				chromosomes[index]=Chromosome(index,arr[y][x][0],arr[y][x][1],arr[y][x][2],-1,y,x,-1)
				index+=1

		# Checking if the size of the image is sufficient to hide the text
		if len(cipher)>(row*column):
			print("The image will not be able to hide the secret")
			print("Try with some bigger image")
		else:
			print("The image will be able to hide the secret")
			a=arr[:]
			count=0
			for i in range(row):
			    for j in range(column):
			        for k in range(len(chromosomes)):
			            if chromosomes[k].getX()==i and chromosomes[k].getY()==j:
			                a[i][j][0]=chromosomes[k].getGene(0)
			                a[i][j][1]=chromosomes[k].getGene(1)
			                a[i][j][2]=chromosomes[k].getGene(2)
			print('Genetic algo completed execution')
			final_img=Image.fromarray(a)
			final_img.save('final'+str(number)+'.png')


			# Visual cryptography
			print("Visual cryptography algorithm started")
			objVisual=visual_cryptography("final"+str(number)+".png",number)
			# This is the key to decrypt the visual crypto image
			keyVisual=objVisual.encrypt()


			# Now generating the pixel index table
			print("Generating the pixel table")
			pitTable=[]
			for i in range(len(cipher)):
			    pitTable.append(Pit())
			pitTableIndex = 0

			for i in range(len(cipher)):
			    for j in range(len(chromosomes)):
			        if chromosomes[j].getSolutionId()==i:
			            test=chromosomes[j].getAllGenes()                
			            minDxs = getMinDx(chromosomes[j].getAllGenes(),cipher[i])
			            pitTable[pitTableIndex] = Pit(chromosomes[j].getX(),chromosomes[j].getY(),minDxs)
			            pitTableIndex+=1 
			for i in range(len(pitTable)):
			    f = open("pit"+str(number)+".csv",'a')
			    f.write(pitTable[i].toString()+"\n")
			f.close()
			print("Pixel Index Table has been built")
			print('The key for decryption of the visual cryptography is: ',keyVisual)
			print('The key for decryption of message is: ',key.decode('utf-8'))


			# Storing the passwords in a file for reference
			pass1='The key for decryption of the visual cryptography is:'+keyVisual
			pass2='The key for decryption of message is:'+key.decode('utf-8')
			file=open('Passwords'+str(number),'w')
			file.write(pass1)
			file.write('\n')
			file.write(pass2)
			print('The keys for decryption are stored in Passwords file in the same folder as this code.')










