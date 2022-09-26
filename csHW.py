#Q1 Input a number and check if the number is prime or composite number.
def CheckPrime(x):
	if x == 2:
		return "2 is a Prime Number."

	for i in range(2,x):
		if x%i == 0 and x != 2:
			return f"{x} is a Composite Number."
			break
		else:
			return f"{x} is a Prime Number."

if __name__ == "__main__":

	#Q1 Input a number and check if the number is prime or composite number.
	print("Q1 Input a number and check if the number is prime or composite number.\n")
	x = int(input("Enter a number: "))
	if (x >= 0):
		print("Neither Prime nor Composite") if x == 1 or x == 0 else print(CheckPrime(x))
	

	#Q2 Count and display the number of vowels consonants, uppercase, lowercase characters in string
	print("Q2 Count and display the number of vowels consonants, uppercase, lowercase characters in string\n")
	vowels = ['a','e','i','o','u']
	st = str(input("Enter a string: "))
	lc, uc, v = 0, 0, 0
	for i in st:
		if (i.lower() in vowels):
			v = 1 + v
		if (i.isupper()):
			uc = 1 + uc
		if (i.islower()):
			lc = 1 + lc
	print(f"No of Vowels = {v}\nNo of consonants = {len(st) - v}\nNo of Uppercase = {uc}\nNo of lowercase = {lc}")
	

	#Q3 Input a string and determine whether it is palindrome or not; convert the case of characters in a string.
	print("Q3 Input a string and determine whether it is palindrome or not; convert the case of characters in a string.\n")
	palin = input("Enter a String: ")
	if (palin.lower() == palin.lower()[::-1]):
		print(f"'{palin}' is a Palindrome.")
	else:
		print(f"'{palin}' is not a Palindrome")

	print(f"{palin} --> {palin.upper()} (Uppercase)\n{palin} --> {palin.lower()} (Lowercase)")


	#Q4 Find the largest/ smallest number in a list/tuple
	print("Q4 Find the largest/ smallest number in a list/tuple\n")
	list1=[1,2,242,3,25,4,6,54,673,7,6578756,73432,43,5,1234,234,234453,8]
	tuple1=(1,2,3,4,57321,54832,432,65,5432,2342534,532,7646,27674,2647,37246)
	print(f"{list1}\n")
	print(f"Max and Min in List: {max(list1)},{min(list1)}")
	print(f"{tuple1}\n")
	print(f"Max and Min in Tuple: {max(tuple1)}, {min(tuple1)}")


	#Q5 Input a list of numbers and swap element at the even location with the elements at the odd location
	print("Q5 Input a list of numbers and swap element at the even location with the elements at the odd location\n")
	listing = list(map(float, input("Enter Numbers (separated by space): ").split()))
	print(f"Original List: {listing}")
	if len(listing)%2 == 0:
		varlen = len(listing)
	else:
		varlen = len(listing)-1
	
	for i in range(0, varlen, 2):
		listing[i], listing[i+1] = listing[i+1], listing[i]

	print(f"Swaped Elements: {listing}")


	#Q6 Input a list/tuple of elements, search for given element in the list/tuple
	print("Q6 Input a list/tuple of elements, search for given element in the list/tuple\n")
	ch = input("list(l)/tuple(t): ")
	if ch == "l" or ch == "list":
		array = list(map(str, input("Enter Elements (separated by space): ").split()))
	elif ch == "t" or ch == "tuple":
		array = tuple(map(str, input("Enter Elements (separated by space)\nRepeated elements will be taken as a single element: ").split()))

	ob = input("Enter Element to Search: ")
	if ob in array:
		print(f"{ob} is in the list/tuple")
	else:
		print(f"{ob} is not present in the list/tuple")
	

	#Q7 Input a list of numbers and find the smallest and largest number from the list
	print("Q7 Input a list of numbers and find the smallest and largest number from the list\n")
	l1 = list(map(float, input("Enter Numbers (separated by space): ").split()))

	print(f"Max value in the list entered is: {max(l1)}\nMin value in the list entered is: {min(l1)}")
	

	#Q8 Create a dictionary with roll number, name and marks of n students in a class and display the names of students who have scored marks above 75
	print("Q8 Create a dictionary with roll number, name and marks of n students in a class and display the names of students who have scored marks above 75\n")
	dbase = {}
	studentsList = []
	amt = int(input("Enter number of students: "))
	for i in range(0, amt):
		rollno = int(input(f"Enter Roll No. of student {i+1}: "))
		name = input(f"Enter name of student {i+1}: ")
		marks = float(input(f"Enter marks of student {i+1}: "))
		dbase[rollno] = [name, marks]

	for s in dbase:
		if dbase[s][1] > 75.0:
			studentsList.append(dbase[s][0])

	print(f"{studentsList} scored more than 75.")
	

	#Q9 Generate the following patterns using nested loop
	print("Q9 Generate the following patterns using nested loop\n")
	print("STAR PATTERN\n")
	for i in range(1,5):
		print("*"*i )

	print("\nNUMBER PATTERN\n")
	for i in range(5, 0, -1):
		for j in range(1, i+1):
			print(j, end="")
		print("\r")
	

	#Q10 Sum of numbers divisible by 3 and 5 in python between 10 to 100
	print("Q10 Sum of numbers divisible by 3 and 5 in python between 10 to 100\n")
	num3, num5, num35 = 0, 0, 0
	for i in range(10, 101):
		if (i%3 == 0):
			num3 = num3 + i
		if (i%5 == 0):
			num5 = i + num5
		if (i%5 == 0) and (i%3 == 0):
			num35 = num35 + i
	print(f"Sum of numbers divisible by 3 = {num3}\nSum of numbers divisible by 5 = {num5}")
	print(f"Sum of numbers divisible by both, 3 and 5, is: {num35}")
