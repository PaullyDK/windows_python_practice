try:
    print("try")
    print(10/0)
except NameError:
    print("except")
finally:
    print("finally")