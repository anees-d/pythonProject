# while loop = a statment that execute it is block of code, as long as it is condition remain true.

'''name = None
while not name:
    name = input("Enter your name: ")

print("Hello "+name)'''
import time

'''while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        print("Stopping loop...")
        break
    print("You entered:", num)'''

# for lopp= execute block of code that a limited amount of time.
# while loop = unlimited
# For loop =  limited

#for i in range(10):
    #print(i+1)

#for i in range(50, 100+1,2):
    #print(i)

for i in "Bro Code":
    print(i)

for seconds in range(10,0,-1):
    print(seconds)
print("Happy new year")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)



for char in "Python":
    print(char)
# skip

for num in range(1, 6):
    print(num)


for num in range(1, 6):
    if num == 3:
        print("Skipping", num)
        continue
    print(num)

for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")
    print()
