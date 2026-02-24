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