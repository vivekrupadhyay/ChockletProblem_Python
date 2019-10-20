Rupees=int(input("Enter Rupees"))			#5 Rupees
count,wrapper=0,0

for i in range(Rupees):
	count +=1
	wrapper +=1
	if wrapper==3:
		count+=1
		wrapper -=2
print(count)