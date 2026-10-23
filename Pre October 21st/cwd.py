import os
cwd = os.getcwd()
print("Current Working Directory:", cwd)

os.mkdir("mysub")
print("mysub directory created in cwd")

os.mkdir("mysub/mysub2")
print("mysub2 created inside mysub")