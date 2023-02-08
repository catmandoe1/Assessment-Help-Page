targetX = 2
targetY = 2

for x in range(0, 10):
	for y in range(0, 5):
		if targetX == x:
			if targetY == y:
				print("Found target!")
				
print("finished")

word = input("Enter a word: ")
length = len(word)
print(length)

# len() of array

grades = ["D", "C", "B", "A"]
amtGrades = len(grades)
print("Amount of possible grades:", amtGrades)

# returned 4

for i in range(0, 4):
	print("Hello, world!")

array = [1, 5, 6, 1, 3, 9]

total = 0
for i in range(0, len(array)): # goes through all elements in the array
	total = total + array[i] # adds each element to the total
	
print(total)