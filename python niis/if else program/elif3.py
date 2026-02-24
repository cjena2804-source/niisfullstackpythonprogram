#wap take a number from keyboard check number is sd dd td od +ve number check"
print("enter a number")
no=int(input())
if no<=9:
	print("sd")
elif no<=99:
	print("dd")
elif no<1000:
	print("td")
elif no>1000:
	print("od")
else:
	print("+ve")