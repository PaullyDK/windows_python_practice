def even_odd(num):
    if num % 2 == 0:
        print(num, "is an even number.")
    else:
        print(num, "is an odd number.")

even_odd(3)

def factorial(num):
    if num < 2:
        return 1
    else: 
        return num * factorial(num - 1)
    
print(factorial(6))

