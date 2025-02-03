# logical operator = and , or and not, to check the condition is true.

temp = int(input("what is the temperature outside: ? "))

if temp>= 0 and temp<= 30:
    print("Temp is good today: ")
    print("Go outside: ")

elif temp < 0 or temp > 30:
    print("temp is bad today: ")
    print("stay inside: ")


temps = [20, 25, 30, 35]

if 30 in temps and 40 not in temps:
    print("30 is in the list, but 40 is not.")  # This will print


