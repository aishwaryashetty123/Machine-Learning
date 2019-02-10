#Single layer perceptron model

x1=[1,-1,1,-1]
x2=[1,1,-1,-1]
t=[1,-1,-1,-1]			#targets of AND

w=[0,0]				#initialize weights and bias
b=0
a=1

def out(x1,x2):			
	yin=b+x1*w[0]+x2*w[1]          #calculate yin
	return -1 if yin<=0 else 1     #return y
		
def model():
	global b,w,x1,x2,t,a
	for i in range(len(x1)):
		print ("Input: ",x1[i],",",x2[i])
		
		while out(x1[i],x2[i])!=t[i]:
			#update weights
			w[0]=w[0]+a*t[i]*x1[i]
			w[1]=w[1]+a*t[i]*x2[i]
			b=b+a*t[i]

		print ("Weights: ",w)
		print ("Bias: ",b)
		print ("Output: ",t[i],"\n")


model()
