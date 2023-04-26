#opening the integers file
my_file = open("integers.txt","r")

#creating two files separating the square of even and cube of odd integers
numbers = [int(x) for x in my_file.read().split()]

#write square numbers to double.txt
with open("double.txt", "w") as square_file:
    for num in numbers:
        if num % 2 == 0:
            square_file.write(str(num**2) + '\n')

#write cube numbers to triple.txt
with open("triple.txt", "w") as cube_file:
    for num in numbers:
        if num % 2 != 0:
            cube_file.write(str(num**3) + '\n')

#creating the header
print("WELCOME TO SQUARE OF EVEN AND CUBE OF ODD INTEGERS PROGRAM")

#creating options
print("Main Menu")
print("1.Square of Even Integers")
print("2.Cube of Odd Integers")
print("3.Exit")
