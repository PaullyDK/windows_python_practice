def f1():
    print("The function f1 is now executing!")

# This check sits at the root level of the script, not inside the function
if __name__ == '__main__':
    print("The code executed directly as a program")
    f1()  # Run your code logic here
else:
    print("The code was imported as a module by another script")
