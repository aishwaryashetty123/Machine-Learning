import random

attributes=[["Sunny","Rainy"],["Warm","Cold"],["Normal","High"],["Strong","Weak"],["Warm","Cool"],["Same","Change"]]
num_attributes=len(attributes)
h=["0"]*num_attributes

def getRandomTrainingExamples(target_concept=["?"]*num_attributes):
	training_ex=[]
	classification=True
	for i in range(num_attributes):
		training_ex.append(attributes[i][random.randint(0,1)])
		if target_concept[i]!="?" and target_concept[i]!=training_ex[i]:
			classification=False
	return training_ex,classification

def findS(training_ex,classification):
	if classification==True:
		for i in range(num_attributes):
			if h[i]=="0":
				h[i]=training_ex[i]
		for i in range(num_attributes):
			if h[i]!=training_ex[i]:
				h[i]="?"

def main():
	target_concept=["Sunny","Warm","?","Strong","?","?"]
	training_examples=[]
	number=50
	for i in range(number):
		training_examples.append(getRandomTrainingExamples(target_concept))
		print(training_examples[i])
		findS(training_examples[i][0],training_examples[i][1])
	print(h)

if __name__=='__main__':
	main()