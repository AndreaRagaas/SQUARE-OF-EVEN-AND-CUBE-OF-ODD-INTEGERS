#2022-09805-MN-0
#RAGAAS, ANDREA 
#BSCPE 1-5
#A method in python that will create two separate text files after reading the source text file named integers.txt that contains 20 integers. The first output file will be named double.txt contains the square of all even integers in integers.txt and the second file will be named triple.txt contains the cube of all odd numbers in the integers.txt.

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

#creating an area to put the option
def MENU():
    while True:
        try:
            choice = int(input("Enter the Choice:"))
            #creating the program for every option
            if choice == 1:
                print("SQUARE OF EVEN INTEGERS")
                with open('double.txt', 'r') as square:
                    for line in square:
                        print(line.strip())
            elif choice == 2:
                print("CUBE OF ODD INTEGERS")
                with open('triple.txt', 'r') as cube:
                    for line in cube:
                        print(line.strip())
            elif choice == 3:
                print("Goodbye!")
                return
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 3.")
            
MENU()

#close the file
my_file.close()