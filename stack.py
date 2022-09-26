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