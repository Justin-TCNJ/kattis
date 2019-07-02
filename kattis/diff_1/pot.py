total = 0
for i in range(int(input())):
	temp = input()
	power = int(temp[-1])
	number = int(temp[0:-1])
	total += number**power
	
print(total)

			

