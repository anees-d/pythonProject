# if statment =  a block of code that will execute if it is condition is true.

age = int(input("How old are you: ? "))

if age == 100:
    print("you are the century old:")
elif age >= 18:
    print("you are the adult:")
elif age < 0:
    print("You have not born yet:")
else:
    print("You are the child:")