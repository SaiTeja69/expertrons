a=[i for i in input("enter list a").split()]
b=[i for i in input("enter list b").split()]
c_dict={}
c=[]
for i in a:
	c_dict[i]=0
for i in b:
	c_dict[i]=0
for i in a:
	c_dict[i]+=1
for i in b:
	c_dict[i]+=1
for i in c_dict.items():
	if i[1]==1:
		c.append(i[0])
print(c)
