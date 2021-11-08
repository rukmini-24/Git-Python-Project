def palindrome(n):
	sum=0
	while(n!=0):
		r=n%10
		sum=sum*10+r
		n=n//10
	return sum

n=int(input("enter a number"))
s=n
t=palindrome(n)
if(t==s):
	print("palindrome")
else:
	print("not a palindrome number")