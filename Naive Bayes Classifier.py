# Naive bayes classifier

import pandas as pd

data=pd.read_csv("training_examples.csv")

def totalcount(data):
	
	a=float((data.play=='Yes').sum())/((data.play).count())
	b=float((data.play=='No').sum())/((data.play).count())
	return a,b

def positive(data,a):
	df=(data[data.play=='Yes'])
	c=float((df.outlook=='Sunny').sum())/len(df)
	d=float((df.Temperature=='Cool').sum())/len(df)
	e=float((df.Humidity=='High').sum())/len(df)
	f=float((df.Wind=='Strong').sum())/len(df)
	pos=a*c*d*e*f
	return pos 
	
def negative(data,b):
	df=(data[data.play=='No'])
	g=float((df.outlook=='Sunny').sum())/len(df)
	h=float((df.Temperature=='Cool').sum())/len(df)
	i=float((df.Humidity=='High').sum())/len(df)
	j=float((df.Wind=='Strong').sum())/len(df)
	neg=b*g*h*i*j
	return neg 


def classify():
	a,b=totalcount(data)
	totalpos=positive(data,a)
	totalneg=negative(data,b)
	if totalpos>totalneg:
		print("Positive")
		norm_pos=totalpos/(totalpos+totalneg)
		print(norm_pos)
	else:
		print("Negative")
		norm_neg=totalneg/(totalpos+totalneg)
		print(norm_neg)

def callfunctions():
	classify()

if __name__ == '__main__':
	callfunctions()