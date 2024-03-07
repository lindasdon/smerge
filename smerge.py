from random import randint
def merge(n1: list, n2: list):
	ret=[]
	place1=place2=0
	while (place1<len(n1)) and (place2<len(n2)):
		if n1[place1]<n2[place2]:
			ret.append(n1[place1])
			place1+=1
		else:
			ret.append(n2[place2])
			place2+=1
	while place1<len(n1):
		ret.append(n1[place1])
		place1+=1
	while place2<len(n2):
		ret.append(n2[place2])
		place2+=1
	return ret
def smerge(n: list):
	half = int(len(n)/2);
	if(half==0):
		return n
	half1=n[:half]
	half2=n[half:]
	return merge(smerge(half1),smerge(half2))

testlist=[randint(0,100) for i in range(10)]
print(str(smerge(testlist)))
