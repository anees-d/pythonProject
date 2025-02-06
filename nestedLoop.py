

rows = int(input("how many rows: ? "))
columns = int(input("How many columns: ? "))
symbol  = input("enter a symbol to use: ")


for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()


for i in range(1, 4):  # Outer loop (rows)
    for j in range(1, 4):  # Inner loop (columns)
        print(i * j, end=" ")  # Multiply row and column values
    print()  # Newline after each row

# nested while

i = 1
while i <= 3:  # Outer loop
    j = 1
    while j <= 3:  # Inner loop
        print(f"({i}, {j})", end=" ")
        j += 1
    print()  # Newline
    i += 1

# right triangle

for i in range(1, 6):  # Outer loop for rows
    for j in range(i):  # Inner loop for columns
        print("*", end=" ")
    print()  # Newline after each row


# creating te chess board:

for i in range(8):  # Rows
    for j in range(8):  # Columns
        if (i + j) % 2 == 0:
            print("⬛", end=" ")  # Black square
        else:
            print("⬜", end=" ")  # White square
    print()  # Newline after each row
