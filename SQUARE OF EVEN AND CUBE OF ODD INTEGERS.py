#opening the integers file
my_file = open("integers.txt","r")

#creating two files separating the square of even and cube of odd integers
numbers = [int(x) for x in my_file.read().split()]
