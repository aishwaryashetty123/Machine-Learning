# Back Propagation Model

import math
x=[0.6,0.8,0.0]
w0=-1
w=[-1,1,2]
v0=[0,0,-1]
v=[[2,1,0],[1,2,3],[0,2,1]]
a=0.3
t=0.9

#Feedforward

def hidden(vj,vij):
	zin=[]
	z=[]
	for i in range(len(vij)):
		zin.append(vj[i]+x[0]*vij[i][0]+x[1]*vij[i][1]+x[2]*vij[i][2])
		print("Zin",i+1,"=",zin[i])
		z.append(1/(1+math.exp(-zin[i])))
		print("Z",i+1,"=",z[i])
	return z 

def response(z,w):
	yin=w0+z[0]*w[0]+z[1]*w[1]+z[2]*w[2]
	print("Yin=",yin)
	y=1/(1+math.exp(-yin))
	print("Y=",y)
	return y

#Back propagation of error	

def errorresponse(y,t):
	d=(t-y)*y*(1-y)
	print("d=",d)
	return d 
	
def errorhidden(d,w,z):
	d1=[]
	d2=[]
	for i in range(len(w)):
		d1.append(d*w[i])
	print("delta=",d1)
	for i in range(len(d1)):
		d2.append(d1[i]*z[i]*(1-z[i]))
	print("error=",d2)
	return d2

#Weight updation
	
def updatew(w,a,d,z):
	wn=[]
	for i in range(len(w)):
		wn.append(w[i]+a*d*z[i])
	print("updated w=",wn)
	return wn
	
def updatew0(w0,a,d):
	return (w0+a*d)
	
def updatev(v,a,d1,x):
	vn=[]
	for i in range(len(v)):
		v1=v[i]
		for j in range(len(v1)):
			v1[j]=v1[j]+a*d1[i]*x[j]
		vn.append(v1)
	print("updated v=",vn)
	return vn

def updatev0(v0,a,d1):
	for i in range(len(v0)):
		v0[i]=v0[i]+a*d1[i]
	print("updated v0=",v0)
	return v0
	
if __name__=="__main__":
	z=hidden(v0,v)
	y=response(z,w)
	for k in range(3):
		print("\nNext iteration\n")
		if (y==t):
			print("Model is learnt")
		else:
			d=errorresponse(y,t)
			d1=errorhidden(d,w,z)
			w=updatew(w,a,d,z)
			w0=updatew0(w0,a,d)
			print("upated w0=",w0)
			v=updatev(v,a,d1,x)
			v0=updatev0(v0,a,d1)
			z=hidden(v0,v)
			y=response(z,w)
		
	
		
