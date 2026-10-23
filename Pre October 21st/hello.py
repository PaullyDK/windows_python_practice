s = input("Enter main string: ")
sub = input("Enter substring: ")
flag = False
pos = -1
n = len(s)
while True:
    pos = s.find(sub, pos + 1, n)
    if pos == -1:
        break
    flag = True
    print(f"Substring found at index: {pos}")

if not flag:
    print("Substring not found.")