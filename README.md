# Integer Manipulation Program

This program is designed to read a source text file named `integers.txt` that contains 20 integers. It then creates two separate output text files based on the contents of the source file. The first output file, named `double.txt`, contains the square of all even integers from `integers.txt`. The second output file, named `triple.txt`, contains the cube of all odd numbers from `integers.txt`. Additionally, the program provides a user interface with a menu that allows you to view the contents of the output files.

## Usage

1. Prepare a source text file named `integers.txt` that contains 20 integers.
2. Run the program.
3. The program will automatically create two output text files: `double.txt` (containing the square of even integers) and `triple.txt` (containing the cube of odd numbers).
4. The program will display a menu with the following options:
   - 1. Square of Even Integers: View the contents of `double.txt`.
   - 2. Cube of Odd Integers: View the contents of `triple.txt`.
   - 3. Exit: Terminate the program.
5. Enter the corresponding number for the desired option and press Enter.
6. If you choose option 1 or 2, the program will display the contents of the respective output file.
7. To exit the program, choose option 3 from the menu.

## File Manipulation

The program opens the `integers.txt` file and reads its contents, storing the integers in a list. It then creates the `double.txt` and `triple.txt` files and writes the calculated square and cube values, respectively, based on the even and odd numbers from the list.

## Menu Interface

The program provides a menu-based user interface that allows you to select various options:

- Square of Even Integers: Displays the contents of `double.txt`, which contains the square of all even integers from `integers.txt`.
- Cube of Odd Integers: Displays the contents of `triple.txt`, which contains the cube of all odd numbers from `integers.txt`.
- Exit: Terminates the program and closes all files.

## Running the Program

To run the program, ensure that the source text file `integers.txt` is present in the same directory as the Python script. Then, execute the script in a Python environment. The program will create the output files and display the menu. Choose an option from the menu to view the respective contents of the output files. To exit the program, select the "Exit" option from the menu.
