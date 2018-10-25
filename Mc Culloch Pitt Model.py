#Mc Culloch Pitt Model

x1=[0,0,1,1]
x2=[0,1,0,1]
w=[1,1]

def out(x1,x2):		
	yin=x1*w[0]+x2*w[1]        #calculate yin
	return 0 if yin<2 else 1   #return y
	
def model():
	for i in range(len(x1)):
		print ("Input: ",x1[i],",",x2[i])
		print ("Output: ",out(x1[i],x2[i]),"\n")

model()