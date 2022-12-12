from random import randint
import pickle
import csv

#Q1
def SI(p, r, t):
	return (p*r*t)/100

#Q2
def oddeven(num):
	if num%2 != 0:
		return "Odd"
	else:
		return "Even"

#Q3
def grader(m):
	if m <= 32:
		return "E"
	elif m >= 33 and m <= 40:
		return "D"
	elif m >= 41 and m <= 60:
		return "C"
	elif m >= 61 and m <= 80:
		return "B"
	elif m >= 81 and m <= 100:
		return "A"
	else:
		return "Out of range."

#Q4
def removeOdd(list1):
	for i in list1:
		if i%2 != 0:
			list1.remove(i)
	
	return list1

#Q6
def occCount(s, l):
	count = 0
	for i in s:
		if i == l:
			count += 1

	return count

#Q7
def nSum(n):
	return (n*(n+1))/2

#Q13
def dice():
	return randint(1,6)
#Q15
def Append(stack):
	if len(stack) >= 10:
		print("OverFlow!")
	else:
		x = input("Enter an element to add: ")
		stack.append(x)
		print("Element added.")
	
def Peek(stack):
	if len(stack) > 0:
		print(stack[-1])
	else:
		print("The stack is empty.")
	
def Display(stack):
	if len(stack) > 0:
		for i in stack:
			print(i, end=", ")
		print("\n")
	else:
		print("The stack is empty.")
	
def Pop(stack):
	x = input("Enter element to Remove: ")
	if x in stack:
		stack.remove(x)
		print("Element Removed.")
	else:
		print("Element does not exist.")

if __name__ == "__main__":
	#1 WAP for calculating simple interest.
	p = float(input("Enter the principal amount: "))
	r = float(input("Enter the rate of interest: "))
	t = float(input("Enter the time period(in years): "))

	print(f"The simple interest would be: {SI(p,r,t)}")
	
	#2 WAP to accept a number from the user and display whether it is an even number or odd number.
	num = int(input("Enter a number to check if it is Odd/Even: "))
	print(f"The given number '{num}' is {oddeven(num)}")

	#3 Write a function in Python to accept percentage of a student and display its grade accordingly.
	m = float(input("Enter the percentage of the student: "))
	
	print(f"The grade is {grader(m)}")

	#4 Write a function to remove all odd numbers from the given list. Where list is passed as an argument.
	list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	print(f"Filtered list is: \n{removeOdd(list1)}")

	#5 WAP to display second largest element of a given list
	list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	print(f"The second largest number in the list is: {sorted(list1)[-2]}")

	#6 Write a Python function to determine how many times a given letter occurs in a string.
	str1 = input("Enter a string: ")
	let = input("Enter a letter to count the occourance of that letter: ")
	
	print(f"'{let}' was repeated {occCount(str1, let)} time(s).")

	#7 Write a program using a user defined function that displays sum of first n natural numbers, where n is passed as an argument.
	n = int(input("Enter n for sum of n natural numbers: "))

	print(f"The sum of first {n} natural numbers is: {nSum(n)}")

	#8 Read a text file line by line and display each word separated by a #.
	with open("file.txt", "r") as fp:
		line = fp.readlines()
		
		for l in line:
			word = l.split(' ')
			print("#".join(word))

	#9 Read a text file and display the number of vowels/consonants/uppercase/lowercase characters in the file.
	with open("file.txt", 'r') as fp:
		line = fp.read()

		vowels = ['a','e','i','o','u']
		lc, uc, v, c = 0, 0, 0, 0
		for i in line:
			if (i.lower() in vowels):
				v += 1
			if (i.isupper()):
				uc += 1
			if (i.islower()):
				lc += 1
			if (i.lower() not in vowels and "a" < i.lower() < "z"):
				c += 1

		print(f"No. of Vowels: {v},\nNo. of Consonant: {c},\nNo. of Uppercase letters: {uc},\nNo. of Lowercase letters: {lc}")

	#10 Remove all the lines that contain the character 'a' in a file and write it to another file.
	f = open('file1.txt', 'r')
	lines = f.readlines()
	f.close()
	with open("file1.txt", "w") as ff:
		with open("filenew.txt", "w") as sf:
			for l in lines:
				if 'a' in l:
					sf.write(l)
				else:
					ff.write(l)

	#11 Create a binary file with name and roll number. Search for a given roll number and display the name, if not found display appropriate message.
	with open("binary.dat", 'wb') as binf:
		pickle.dump(['John Doe', 1001], binf)
		pickle.dump(['Jane Doe', 1002], binf)
		pickle.dump(['Jack Doe', 1003], binf)

	x = int(input("Enter a roll number to search: "))
	found = False
	with open("binary.dat", 'rb') as rbin:
		while 1:
			try:
				rd = pickle.load(rbin)
				if rd[1] == x:
					print(f"Roll No. and Name: {rd[1]}, {rd[0]}")
					found = True
			except EOFError:
				break
		
		if found != True:
			print("Record Not Found.")

	#12 Create a binary file with roll number, name and marks. Input a roll number and update the marks.


	#13 Write a random number generator that generates random numbers between 1 and 6 (simulates a dice).
	while 1:
		c = input("Roll a dice? (y/N): ")
		if c.lower() == "y":
			print(f"You got: {dice()}")
		else:
			break

	#14 Create a CSV file by entering user-id and password, read and search the password for given user-id.
	with open("manager.csv", 'w') as mng:
		w = csv.writer(mng)
		w.writerow(['user-id','password'])

		while 1:
			ui = input("Enter user-id: ")
			pwd = input("Enter password: ")

			w.writerow([ui,pwd])
			c = input("Add more? (y/N): ")
			if c.lower() == "n":
				break
	
	srch = input("Enter user-id to search: ")
	found = False
	with open("manager.csv", 'r') as rdr:
		r = csv.reader(rdr)
		for i in r:
			next(r)
			if i[0] == srch:
				print(f"User-id: {srch}, Password: {i[1]}")
				found = True

		if found == False:
			print("User-id not found.")			

	#15 Write a Python program to implement (Push, Pop, Peek and display) a stack using list.
	stack = []
	print("Stack Program\n")
	while 1:
		print("Menu\n")
		x = input("Enter a Choice: \n(a) Append\n(d) Display\n(p) Peek\n(r) pop\n(e) Exit\n>>> ")
		if x == "e":
			break
		elif x == "a":
			Append(stack)
		elif x == "p":
			Peek(stack)
		elif x == "d":
			Display(stack)
		elif x == "r":
			Pop(stack)
		else:
			print("Invalid Choice. Try Again.")

