attributes=[["Sunny","Rainy"],["Warm","Cold"],["Normal","High"],["Strong","Weak"],["Warm","Cool"],["Same","Change"]]
num_attributes=len(attributes)
S=[["0"]*num_attributes]
G=[["?"]*num_attributes]

def pconsistent(instance):
	global G
	glist=[]
	for i in range(len(G)):
		for j in range(num_attributes):
			if G[i][j]!="?" and instance[j]!=G[i][j]:
				glist.append(G[i])
				break
	for item in glist:
		G.remove(item)

def nconsistent(instance):
	global S
	slist=[]
	for i in range(len(S)):
		flag=True
		for j in range(num_attributes):
			if instance[j]!=S[i][j]:
				flag=False
				break
		if flag:
					slist.append(S[i])
	for item in slist:
		S.remove(item)

def getothervalues(index,value):
	global attributes
	return [x for x in attributes[index] if x!=value]

def generaliseS(instance):
	global S
	for sitem in S:
		if "0" in sitem:
			S.pop()
			S.append(instance)
			break
		else:
			for j in range(num_attributes):
				if sitem[j]!=instance[j]:
					sitem[j]="?"
	newlst=[]
	for item in S:
		if item not in newlst:
			newlst.append(item)
	S=newlst

def specialiseG(instance):
	global G
	glist=[]
	newg=[]
	for gitem in G:
		for j in range(num_attributes):
			if gitem[j]=="?":
				val=getothervalues(j,instance[j])
				for v in val:
					newitem=list(gitem)
					newitem[j]=v
					newg.append(newitem)
				if gitem not in glist:
					glist.append(gitem)
	for item in glist:
		G.remove(item)
	for item in newg:
		G.append(item)
	newlst=[]
	for item in G:
		if item not in newlst:
			newlst.append(item)
	G=newlst

def checkboundaries(type):
	global G
	global S
	if type=="G":
		glist=[]
		for gitem in G:
			for sitem in S:
				for j in range(num_attributes):
					if gitem[j]!=sitem[j] and gitem[j]!="?" and sitem[j]!="0":
						glist.append(gitem)
						break
		for item in glist:
			G.remove(item)
	elif type=="S":
		slist=[]
		for sitem in S:
			for gitem in G:
				for j in range(num_attributes):
					if gitem[j]!=sitem[j] and gitem[j]!="?" and sitem[j]!="0":
						slist.append(sitem)
						break
		for item in slist:
			S.remove(item)
	if len(G)==0:
		S=[]
	elif len(S)==0:
		G=[]




def cea(instance,target):
	if target:
		pconsistent(instance)
		generaliseS(instance)
		checkboundaries("S")
	else:
		nconsistent(instance)
		specialiseG(instance)
		checkboundaries("G")
	
	


def main():
	training_examples=[(["Sunny","Warm","Normal","Strong","Warm","Same"],True),(["Sunny","Warm","High","Strong","Warm","Same"],True),
	(["Rainy","Cold","High","Strong","Warm","Change"],False),(["Sunny","Warm","High","Strong","Cool","Change"],True)]
	for i in range(4):
		cea(training_examples[i][0],training_examples[i][1])
	print(S)
	print(G)

if __name__=='__main__':
	main()