# This script will prompt the user to enter a positive integer, 
# then use nested loops to print a square pattern of that size made of asterisks (*)

pattern_size = int(input("Enter the size of the pattern: "))
intial = 0
while intial < pattern_size:
    for i in range(pattern_size):
        print("*", end="")
    print('\n')
    intial += 1
